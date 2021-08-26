# Python WGS84-Conveter
Converts latitude and longitude units into how many meters the coordinate is from a set origin point. Based on the C# version from IndoorAtlas SDK.

## Example

```
from WGSConversion import *

converter = WGSConversion()

converter.setOrigin(55.69826, 12.54283)

print(converter.WGStoEN(55.69857, 12.54236))
# Output: (1.322640307858514e-18, -9.963479942111962e-06)

print(converter.WGStoEN(55.69964, 12.54395))
# Output: (5.88788266082961e-18, 2.3742760713124275e-05)
```
