# nginx

依赖库：
	1. zlib    zlib-devel
	2. OpenSSL开发库
	3. GCC编译器
	4. PCRE库
```sh
sudo apt-get install -y libz-dev libpcre3-dev libssl-dev
```


编译安装:
```sh
wget http://nginx.org/download/nginx-1.26.0.tar.gz 
tar zxvf nginx-1.26.0.tar.gz
cd nginx-1.26.0
./configure
make
make install
```

查看nginx版本
```sh
/usr/local/nginx/sbin/nginx -v
nginx version: nginx/1.26.0
```

到此，nginx安装完成。