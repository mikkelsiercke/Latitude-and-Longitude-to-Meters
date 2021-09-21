# Python WGS84-Conveter
Converts latitude and longitude units into how many meters the coordinate is from a set origin point. Based on the C# version from IndoorAtlas SDK.

## Example

```
from WGSConversion import *

converter = WGSConversion()

converter.setOrigin(55.69826, 12.54283)

print(converter.WGStoEN(55.69964, 12.54395))
# Output: (153.64413898097823, 70.42337471336053)

print(converter.calculateENLongitude(12.54236))
# Output: -29.552666174348676

print(converter.calculateENLatitude(55.69964))
# Output: 153.64413898097823
```
