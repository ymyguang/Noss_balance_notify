### 前言

想必大家都在挂机Noss,苦于始终关注Noss的更新情况，很麻烦，写了个小脚本，实时查询Noss数量，打到新的Noss后自动推送到WeChat，希望能够帮到大家（尽管打了很长时间了，也打不到

功能：

1. **采用多线程，实时查询**
2. **自动推送到指定微信**
3. **支持查询多个地址钱包**

---

### 使用说明

1. 关注推送渠道

<img src="https://wxpusher.zjiecode.com/api/qrcode/Ilo2cJrgCotr2zvJcBmpNfI91vTjnLNh71HMuA4g3njsH8BktHperDljx3HTe3Vh.jpg" alt="应用二维码" style="zoom:50%;" />
（若二维码失效，在微信打开链接：https://wxpusher.zjiecode.com/wxuser/?type=1&id=68685#/follow）

2. 获取自己的UID

<img src="C:\Users\admin.000\AppData\Roaming\Typora\typora-user-images\image-20240102230551973.png" alt="image-20240102230551973" style="zoom:33%;" />

3. 代码中输入自己的地址和UID

如：

```python
ADDRESS_LIST = {
    "address1",
    "address2"
}
UUID = "UID_********"
```

---

### 感谢wxpusher提供推送平台
