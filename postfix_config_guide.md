# Cisco Sustainability Intel Briefing - Postfix Configuration Guide
# 配置日期：2026年3月16日

## 步骤 1：创建 SMTP 认证配置

运行以下命令创建认证文件：

```bash
# 创建配置文件（需要 sudo 权限）
sudo touch /etc/postfix/sasl_passwd

# 设置权限（只有 root 可读写）
sudo chmod 600 /etc/postfix/sasl_passwd
```

## 步骤 2：添加 SMTP 服务器信息

编辑文件 /etc/postfix/sasl_passwd，添加以下内容：

```
[smtp.cisco.com]:587 dit2@cisco.com:YOUR_PASSWORD_OR_APP_PASSWORD
```

**说明：**
- `[smtp.cisco.com]`: Cisco SMTP 服务器地址
- `587`: SMTP 端口（Submission 端口，支持 TLS）
- `dit2@cisco.com`: 你的邮箱
- `YOUR_PASSWORD_OR_APP_PASSWORD`: 邮箱密码或应用专用密码

**编辑命令：**
```bash
sudo nano /etc/postfix/sasl_passwd
```
粘贴上述内容，替换密码，保存退出。

## 步骤 3：创建 Postfix 映射文件

```bash
sudo postmap /etc/postfix/sasl_passwd
```

这会生成 sasl_passwd.db 文件。

## 步骤 4：配置 Postfix 使用 SMTP 服务器

编辑 Postfix 主配置文件：

```bash
sudo nano /etc/postfix/main.cf
```

**在文件末尾添加以下内容：**

```
# Cisco SMTP Configuration
relayhost = [smtp.cisco.com]:587

# Enable SASL authentication
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
smtp_sasl_security_options = noanonymous

# Enable TLS
smtp_tls_security_level = encrypt
smtp_tls_CAfile = /etc/ssl/cert.pem
```

## 步骤 5：更新 Postfix 配置

```bash
sudo postfix reload
```

## 步骤 6：测试发送邮件

```bash
echo "Test email from Postfix" | mail -s "Postfix Test" dit2@cisco.com
```

## 步骤 7：查看邮件发送状态

如果邮件没有收到，查看日志：

```bash
sudo tail -f /var/log/mail.log
```

## 常见问题

### 1. 认证失败
检查密码是否正确，或考虑使用应用专用密码。

### 2. TLS 证书错误
尝试更新 CA 文件路径：
```
smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt
```

### 3. 防火墙阻止
确保 587 端口未被防火墙阻止。

---

**配置完成后，请告诉我测试邮件是否收到。**
