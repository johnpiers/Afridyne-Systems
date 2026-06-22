---
# This tells MkDocs to ignore the 'caption' features for this page
caption:
  figure:
    enable: false
  table:
    enable: false
  custom:
    enable: false
---

![AMD Ryzen™ AI Software](https://www.amd.com/content/dam/amd/en/images/logos/products/2833999-ryzen-ai-software-logo-banner-developer.jpg)

# XDNA
## Generate bindings for xdna-driver
```
$ bindgen --no-layout-tests --wrap-unsafe-ops header/amdxdna_accel.h > bindings.rs
```

### Header source
<https://github.com/amd/xdna-driver/blob/main/src/include/uapi/drm_local/amdxdna_accel.h>

[Back to AMDgpu-Top Main Page](../../../../../AMDgpu-Top.md)