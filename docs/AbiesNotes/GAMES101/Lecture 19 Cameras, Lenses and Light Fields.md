Imaging = Synthesis + Capture

### Field of View (FOV)

![FOV](../resources/FOV.png){style="width:400px"}

For a fixed sensor size, decreaseing the focal length increses the FOV.

$$\text{FOV}=2\,\arctan\left(\frac{h}{2f}\right)$$

Due to historical reasons, the angle of view is usually expressed using the focal length of lenses designed for 35mm format film (36 x 24mm).

- 17mm is a wide-angle lens, with a field of view of 104°
- 50mm is a "standard" lens, with a field of view of 47°
- 200mm is a telephoto lens, with a field of view of 12°

### Exposure

$H=T\times E$ (Exposure = Time $\times$ Irradiance)

Exposure time T: controlled by shutter  
Irradiance E: power of light falling on a unit area of sensor. Controlled by lens aperture and focal length.

**Aperture size**

- Change the f-stop by opening / closing the aperture

**Shutter speed**

- Change the duration the sensor pixels integrate light

**ISO gain**

- Change the amplification (analog and/or digital) between sensor values and digital image values

![camera exposure](../resources/camera%20exposure.png){style="width:500px"}


#### ISO (Gain)

Third vaiable for exposure

Film: trade sensitivity for grain  
Digital: trade sensitive for noise

- Multiply signal before analog-to-digital conversion  
- Linear effect (ISO 200 needs half the light as ISO 100)

#### F-Number (F-Stop)

Written as FN or F/N. N is the f-number.

Informal understanding: the inverse-diameter of a round aperture.

Formal definition: the focal length divided by the diameter of the aperture.

#### Shutter

Motion blur: handshake, subject movement.  
Doubling shutter time doubles motion blur.

**Rolling shutter:** different parts of photo taken at different times.

If the exposure is to  bright/dark, may need to adjust f-stop and/or shutter up/down.

Photograhers must trade off depth of field and motion blur for moving subjects.

**High-speed photography:** extremely fase shutter speed x (large aperture and/or high ISO)

### Thin Lens Approximation

We consider focal length can be arbitrarily changed (in reality, yes)

Gaussian thin lens equation:

$$\frac{1}{f}=\frac{1}{z_i}+\frac{1}{z_o}$$

(Why? Draw parallel ray and focal ray)

#### Defocus Blur

**Circle of Confusion (CoC)**

When the object is not on the focal plane, the image is not on the sensor plane. Sensor recieves a circle of light.

C denotes the diameter of CoC. A denotes the diameter of lens.

![CoC](../resources/CoC.png){style="width:450px"}

$$ \frac{C}{A}=\frac{d'}{z_i}=\frac{|z_s-z_i|}{z_i}$$

$$ C=A\frac{|z_s-z_i|}{z_i}=\frac{F}{N}\frac{|z_s-z_i|}{z_i}$$

**Ray tracing for defocus blur**

- Choose sensoe size, lens focal length and aperture size  
- Choose depth of subject of interest $z_o$

#### Depth of Field

Depth range in a scene where the corresponding CoC is considered small enough.

Depth of field: max depth range - min depth range



