# psb_decode

A Python 3 package to decode PAY by Square QR code data.

## Installation

```bash
pip install pbs_decode
```

## Usage

```python
from pbs_decode import pbs_decode

# Read QR code and decode it
extracted_data = ...
decoded_data = pbs_decode(extracted_data)
```

## Useful links

- [Package to encode PAY by Square QR code data](https://bysquare.com/pay-by-square/)
- [PAY by Square specification](https://www.sbaonline.sk/wp-content/uploads/2020/03/pay-by-square-specifications-1_1_0.pdf)
- [PAY by Square website](https://bysquare.com/pay-by-square/)
