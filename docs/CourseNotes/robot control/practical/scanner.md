## 3D扫描仪使用

**工件前期准备：**

1. 表面处理：深色浅色可以，镜面和玻璃不能直接扫（显像剂…）  
2. 标记点粘贴：平面且曲率小的位置，避免边角等特征点；无规则粘贴，避免共线、等腰三角形（平面拼接）；公共区域的标记点大于 4 个；均匀粘贴  
3. 制定扫描策略（拼接）：激光点拼接，靠特征进行拼接；标记点拼接

**参数：**

1. 点密度：激光点两点之间的距离。数值越大，点越稀疏。精度高 0.2-0.3，标准件 0.5  
2. 曝光值：激光线的亮暗程度。浅色暗（反光多），默认 1；正常 5；深黑色 7  
3. 扫描模式：标记点/激光面片。先扫标记点，再扫面片  
4. 标记点：按大小勾选  
5. 黑亮模式：深色或反光物体勾选  

**扫描过程：**

新建文件，设置参数。按 M 开始扫描。+-使软件上图像放大缩小。一面扫描完后结束，点击添加，翻面继续扫描。

**数据处理：**

1. 背景平面：平面以下删除  
2. 连接项：选主体，反选，删除  
3. 非连接项：选取连接的一片点  
4. 孤立点：孤立的一个点  
    
**合并：**

1. 标记点合并：选中公共面上的标记点  
2. 激光点合并：在公共面上点  
    
**网格化：**

三角面片处理

**保存：**

保存后为网格文件，.stl。封装前为.asc 格式文件。

**标记点颜色状态：**

1. 绿色：当前视野中看到的标记点  
2. 白色：已经扫描完整的点  
3. 蓝色：当前没有扫描到的点  
    
**精细扫描：**

选倍率；点精细扫描，选中扫描区域；点精细扫描，退出；开始扫描。双击 M 切换扫描模式。

## PCL

### main.cpp

```cpp
#include <fstream>

#include "file.h"
#include "visualizer.h"
#include "tools.h"

#include "mls_custom.h"

int main()
{
	std::string read_file_path = "D:/NaiLong1.asc"; // asc格式点云 存储路径
	std::string save_file_path = "D:/NaiLong.ply"; // ply网格数据 存储路径
	
	// 0、读取asc格式点云数据
	pcl::PointCloud<pcl::PointNormal>::Ptr point_cloud;
	if (!readAscFile(read_file_path, point_cloud)) {
		printf("read %s failed!\n", read_file_path.c_str());
		system("pause");
		return -1;
	}
	showPointCloud(point_cloud, true); // 1

	// 1、计算当前点云解析度
	float resolution = compute_resolution(point_cloud);

	// 2、重新计算法向量
	pcl::PointCloud<pcl::PointNormal>::Ptr point_normals;
	compute_normals(point_cloud, resolution, point_normals);
	showPointCloud(point_normals, true); // 2
	// 2.5 校正下法向量
	correct_normals(point_cloud, point_normals);
	showPointCloud(point_normals, true); // 3

	{	// 利用自己修改的代码计算法向量（未作效率优化）
		pcl::PointCloud<pcl::PointNormal>::Ptr mls_normals;
		compute_mls_custom(point_cloud, resolution, mls_normals);
		showPointCloud(mls_normals, true); // 自己修改，不用校正，少了一次全部数据的遍历 // 4
	}

	// 3、剔除离群点
	pcl::PointCloud<pcl::PointNormal>::Ptr sor_points;
	sor_filter(point_normals, sor_points);
	//showPointCloud2ViewPort(point_normals, sor_points); // 如果界面中不显示按下r键，复位下视角
	showPointCloud(point_normals, sor_points); // 5

	// 4、进行mls滤波
	pcl::PointCloud<pcl::PointNormal>::Ptr mls_points;
	mls_filter(sor_points, resolution, mls_points);
	showPointCloud(sor_points, mls_points); // 6
	//showPointCloud(mls_points, true);

	// 5、平面分割
	pcl::PointCloud<pcl::PointNormal>::Ptr seg_points;
	plane_segmentation(mls_points, seg_points);
	showPointCloud(mls_points, seg_points);  // 7

	// 6、网格化
	pcl::PolygonMesh::Ptr poly_mesh;
	triangulation(seg_points, resolution, poly_mesh);
	showPolygonMesh(poly_mesh);
	
	// 7、保存网格数据
	savePlyFile(save_file_path, poly_mesh);

	system("pause");
	return 0;
}
```

### tools.cpp

```cpp
#include "tools.h"

#include <pcl/filters/statistical_outlier_removal.h>
#include <pcl/surface/mls.h>
#include <pcl/surface/gp3.h>
#include <pcl/features/normal_3d.h>
#define PCL_NO_PRECOMPILE // SACSegmentation 未导出PointNormal类型，需要编译模板
#include <pcl/segmentation/sac_segmentation.h >
#include <pcl/filters/extract_indices.h>

/**
* @brief 剔除离群点
* @param [in] point_cloud 待滤波点云
* @param [out] filter_cloud 滤波结果
* @return
*/
void sor_filter(const pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud
	, pcl::PointCloud<pcl::PointNormal>::Ptr& filter_cloud)
{
	/* 参数设置:
	* 每个点要分析的邻居数设置为50，标准差乘数为1。
	* 这意味着，所有到查询点的距离大于1个标准差的点都将被标记为离群值并被删除。
	*/

	filter_cloud = std::make_shared<pcl::PointCloud<pcl::PointNormal>>();

	pcl::StatisticalOutlierRemoval<pcl::PointNormal> sor; // 创建对象
	sor.setInputCloud(point_cloud); // 设置点云
	sor.setMeanK(20); // 设置均值参数k
	sor.setStddevMulThresh(2.0); // 设置阈值
	sor.filter(*filter_cloud);
}

/**
* @brief 计算法向量
* @param [in] point_cloud 输入的点云
* @param [in] resolution 点云解析度
* @param [out] new_cloud 计算法向量后的点云
* @return
*/
void compute_normals(const pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud
	, const float& resolution
	, pcl::PointCloud<pcl::PointNormal>::Ptr& new_cloud)
{
	new_cloud = std::make_shared<pcl::PointCloud<pcl::PointNormal>>();

	// 计算法向量
	pcl::NormalEstimation<pcl::PointNormal, pcl::PointNormal> nest;
	nest.setRadiusSearch(5 * resolution); // 设置拟合时邻域搜索半径，最好用模型分辨率的倍数
	//nest.setKSearch(10); // 设置拟合时采用的点数
	nest.setInputCloud(point_cloud);
	nest.compute(*new_cloud);

	// NormalEstimation 计算法向量的结果，会把点坐标丢掉，需要重新赋值过来
	for (int idx = 0; idx < point_cloud->size(); ++idx) {
		new_cloud->points[idx].getVector3fMap() = point_cloud->points[idx].getVector3fMap();
	}
}

/**
* @brief mls滤波
* @param [in] point_cloud 待滤波点云
* @param [in] resolution 点云解析度
* @param [out] filter_cloud 滤波结果
* @return
*/
void mls_filter(const pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud
	, const float& resolution
	, pcl::PointCloud<pcl::PointNormal>::Ptr& filter_cloud)
{
	filter_cloud = std::make_shared<pcl::PointCloud<pcl::PointNormal>>();

	// 构建kdtree，方便搜索邻域数据
	pcl::search::KdTree<pcl::PointNormal>::Ptr kdtree = std::make_shared<pcl::search::KdTree<pcl::PointNormal>>();
	kdtree->setInputCloud(point_cloud);

	pcl::MovingLeastSquares<pcl::PointNormal, pcl::PointNormal> mls;
	mls.setInputCloud(point_cloud);
	mls.setComputeNormals(false); // 是否计算法向量，如果计算（True），可能会反，则需要校正一下
	mls.setPolynomialOrder(3); //MLS拟合曲线的阶数
	mls.setSearchMethod(kdtree);
	mls.setSearchRadius(5 * resolution); // 拟合曲面搜索半径
	// Reconstruct
	mls.process(*filter_cloud);
}

/**
* @brief 平面分割，剔除平面数据
* @param [in] point_cloud 输入的点云
* @param [out] filter_cloud 分割后结果
* @return
*/
void plane_segmentation(const pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud
	, pcl::PointCloud<pcl::PointNormal>::Ptr& filter_cloud)
{
	filter_cloud = std::make_shared<pcl::PointCloud<pcl::PointNormal>>();

	pcl::SACSegmentation<pcl::PointNormal> seg;
	pcl::PointIndices::Ptr inliers(new pcl::PointIndices);
	pcl::ModelCoefficients::Ptr coefficients(new pcl::ModelCoefficients);
	seg.setOptimizeCoefficients(true);
	seg.setModelType(pcl::SACMODEL_PLANE); // 选择平面
	seg.setMethodType(pcl::SAC_RANSAC); // RANSAC 方法
	seg.setMaxIterations(20); // 最大迭代次数
	//seg.setMaxIterations(50); // 最大迭代次数
	seg.setDistanceThreshold(1.0); // 阈值
	seg.setInputCloud(point_cloud);
	seg.segment(*inliers, *coefficients);

	// 去除平面内点
	pcl::ExtractIndices<pcl::PointNormal> extract;
	extract.setInputCloud(point_cloud);
	extract.setIndices(inliers);
	
	extract.setNegative(true);
	extract.filter(*filter_cloud);
}

/**
* @brief 点云网格化
* @param [in] point_cloud 输入的点云
* @param [in] resolution 点云解析度
* @param [out] poly_mesh 网格数据
* @return
*/
void triangulation(const pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud
	, const float& resolution
	, pcl::PolygonMesh::Ptr& poly_mesh)
{
	poly_mesh = std::make_shared<pcl::PolygonMesh>();

	// 构建kdtree，方便搜索邻域数据
	pcl::search::KdTree<pcl::PointNormal>::Ptr kdtree = std::make_shared<pcl::search::KdTree<pcl::PointNormal>>();
	kdtree->setInputCloud(point_cloud);

	pcl::GreedyProjectionTriangulation<pcl::PointNormal> gp3;
	gp3.setSearchRadius(5 * resolution); // 设置近邻搜索半径
	gp3.setMu(2.5); //设置最近邻距离的乘子，以得到每个点的最终搜索半径
	gp3.setMaximumNearestNeighbors(20); //设置搜索的最近邻点的最大数量
	gp3.setMaximumSurfaceAngle(M_PI / 4); // 45 degrees（pi）最大平面角
	gp3.setMinimumAngle(M_PI / 18); // 10 degrees 每个三角的最小角度
	gp3.setMaximumAngle(2 * M_PI / 3); // 120 degrees 每个三角的最大角度
	gp3.setNormalConsistency(false); //如果法向量一致，设置为true
	
	gp3.setInputCloud(point_cloud);
	gp3.setSearchMethod(kdtree);
	gp3.reconstruct(*poly_mesh);
}

/**
* @brief 计算点云解析度（粗略）
* @param [in] point_cloud 输入的点云
* @return resolution 点云解析度
*/
double compute_resolution(const pcl::PointCloud<pcl::PointNormal>::ConstPtr& point_cloud)
{
	double resolution = 0.0;
	int numberOfPoints = 0;
	int nres;
	std::vector<int> indices(2);
	std::vector<float> squaredDistances(2);

	// 构建kdtree，方便搜索邻域数据
	pcl::search::KdTree<pcl::PointNormal>::Ptr kdtree = std::make_shared<pcl::search::KdTree<pcl::PointNormal>>();
	kdtree->setInputCloud(point_cloud);

	for (size_t i = 0; i < point_cloud->size(); ++i)
	{
		if (std::isnan((*point_cloud)[i].x)) // 剔除nan值
			continue;

		nres = kdtree->nearestKSearch(i, 2, indices, squaredDistances); // 第一个是该点本身
		if (nres == 2)
		{
			resolution += sqrt(squaredDistances[1]);
			++numberOfPoints; // 最近点的距离
		}
	}
	if (numberOfPoints != 0)
		resolution /= numberOfPoints; // 平均距离当作解析度

	return resolution;
}

/**
* @brief 修正点云法向量方向
* @param [in] ref_cloud 参考的点云
* @param [in][out] correct_cloud 待修正的点云
* @return
*/
void correct_normals(const pcl::PointCloud<pcl::PointNormal>::Ptr& ref_cloud
	, pcl::PointCloud<pcl::PointNormal>::Ptr& correct_cloud)
{
	if (nullptr == ref_cloud || nullptr == correct_cloud
		|| ref_cloud->size() != correct_cloud->size()) {
		return;
	}

	for (int idx = 0; idx < ref_cloud->size(); ++idx) {
		const pcl::Vector3fMap& ref_nor = ref_cloud->points[idx].getNormalVector3fMap();
		const pcl::Vector3fMap& correct_nor = correct_cloud->points[idx].getNormalVector3fMap();
		if (ref_nor.dot(correct_nor) < 0) { // 法向量方向反了，需要校正
			correct_cloud->points[idx].normal_x *= -1;
			correct_cloud->points[idx].normal_y *= -1;
			correct_cloud->points[idx].normal_z *= -1;
		}
	}
}
```

### visualizer.cpp

```cpp
#include "visualizer.h"

/**
* @brief 显示点云
* @param [in] point_cloud 待显示点云
* @param [in] show_normals 是否显示法向量
* @return
*/
void showPointCloud(const pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud, bool show_normals)
{
	pcl::visualization::PCLVisualizer viewer; // 定义对象
	viewer.setBackgroundColor(0, 0, 0); // 设置背景颜色，rgb 

	pcl::visualization::PointCloudColorHandlerCustom<pcl::PointNormal> red(point_cloud, 255, 0, 0); // rgb
	// 将点云设置颜色，默认白色
	viewer.addPointCloud<pcl::PointNormal>(point_cloud, red, "point_cloud");

	if (show_normals) {
		int level = 5; // 多少条法向量集合显示成一条
		float scale = 2.0; // 法向量长度
		viewer.addPointCloudNormals<pcl::PointNormal>(point_cloud, level, scale, "point_normals");
	}
	
	viewer.spin(); // 阻塞式显示
}

/**
* @brief 同一个视口，显示两个点云
* @param [in] point_cloud_1 待显示点云1（红色）
* @param [in] point_cloud_2 待显示点云1（绿色）
* @return
*/
void showPointCloud(const pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud_1, 
	const pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud_2)
{
	pcl::visualization::PCLVisualizer viewer; // 定义对象
	viewer.setBackgroundColor(0, 0, 0); // 设置背景颜色，rgb 

	pcl::visualization::PointCloudColorHandlerCustom<pcl::PointNormal> red(point_cloud_1, 255, 0, 0); // rgb
	// 将点云设置颜色，默认白色
	viewer.addPointCloud<pcl::PointNormal>(point_cloud_1, red, "point_cloud_1");
	//将点按照大小为3显示
	viewer.setPointCloudRenderingProperties(pcl::visualization::PCL_VISUALIZER_POINT_SIZE, 3, "point_cloud_1");

	pcl::visualization::PointCloudColorHandlerCustom<pcl::PointNormal> green(point_cloud_2, 0, 255, 0); // rgb
	// 将点云设置颜色，默认白色
	viewer.addPointCloud<pcl::PointNormal>(point_cloud_2, green, "point_cloud_2");
	//将点按照大小为5显示
	viewer.setPointCloudRenderingProperties(pcl::visualization::PCL_VISUALIZER_POINT_SIZE, 5, "point_cloud_2");

	viewer.spin(); // 阻塞式显示
}

/**
* @brief 分左右两个视口，显示两个点云
* @param [in] point_cloud_1 待显示点云1（红色）
* @param [in] point_cloud_2 待显示点云1（绿色）
* @return
* @note 如果不显示按下r键
*/
void showPointCloud2ViewPort(const pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud_1,
	const pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud_2)
{
	// 定义对象
	pcl::visualization::PCLVisualizer viewer;

	int v1(1); // viewport
	viewer.createViewPort(0.0, 0.0, 0.5, 1.0, v1);
	viewer.setBackgroundColor(0, 0, 0, v1);
	pcl::visualization::PointCloudColorHandlerCustom<pcl::PointNormal> red(point_cloud_1, 255, 0 , 0); // rgb
	viewer.addPointCloud<pcl::PointNormal>(point_cloud_1, red, "point_cloud_1", v1);

	int v2(2);// viewport
	viewer.createViewPort(0.5, 0.0, 1.0, 1.0, v2);
	viewer.setBackgroundColor(0, 0, 0, v2);
	pcl::visualization::PointCloudColorHandlerCustom<pcl::PointNormal> green(point_cloud_2, 0, 255, 0); // rgb
	viewer.addPointCloud<pcl::PointNormal>(point_cloud_2, green, "point_cloud_2", v2);

	viewer.spin();
}


/**
* @brief 显示网格数据
* @param [in] poly_mesh 待显示网格数据
* @return
*/
void showPolygonMesh(const pcl::PolygonMesh::Ptr& poly_mesh)
{
	pcl::visualization::PCLVisualizer viewer; // 定义对象

	viewer.addPolygonMesh(*poly_mesh, "poly_mesh");

	viewer.spin();
}
```

### file.cpp

```cpp
#include "file.h"
#include <fstream>

/**
* @brief 读取asc格式点云（x y z nx ny nz）
* @param [in] path 文件路径
* @param [out] point_cloud 读取的点云数据
* @return
*/
bool readAscFile(std::string path, pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud)
{
	std::ifstream in_stream;
	in_stream.open(path);
	if (!in_stream.is_open()) {
		return false;
	}

	point_cloud = std::make_shared<pcl::PointCloud<pcl::PointNormal>>();

	float x, y, z;
	float nx, ny, nz;
	pcl::PointNormal pt;
	while (!in_stream.eof()) {
		in_stream >> x >> y >> z; // 自定义asc格式： x y z nx ny nz
		in_stream >> nx >> ny >> nz;

		if (!in_stream.eof()) {
			pt.x = x; pt.y = y; pt.z = z;
			pt.normal_x = nx; pt.normal_y = ny; pt.normal_z = nz;

			point_cloud->push_back(pt);
		}
	}
	in_stream.close();

	return true;
}

/**
* @brief 保存asc格式点云（x y z nx ny nz）
* @param [in] path 文件路径
* @param [in] point_cloud 保存的点云数据
* @return
*/
bool saveAscFile(std::string path, const pcl::PointCloud<pcl::PointNormal>::Ptr& point_cloud)
{
	std::ofstream out_stream;
	out_stream.open(path);
	if (!out_stream.is_open()) {
		return false;
	}

	for (int idx = 0; idx < point_cloud->size(); ++idx) {
		out_stream
			<< point_cloud->points[idx].x << " "
			<< point_cloud->points[idx].y << " "
			<< point_cloud->points[idx].z << " "
			<< point_cloud->points[idx].normal_x << " "
			<< point_cloud->points[idx].normal_y << " "
			<< point_cloud->points[idx].normal_z << " \n";
	}
	out_stream.close();

	return true;
}

/**
* @brief 保存ply网格数据
* @param [in] path 文件路径
* @param [in] poly_mesh 保存的网格数据
* @return
*/
bool savePlyFile(std::string path, const pcl::PolygonMesh::Ptr& poly_mesh)
{
	int ret = pcl::io::savePLYFileBinary(path, *poly_mesh);
	return (0 == ret);
}
```