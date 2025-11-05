---
title: Access
sidebar_position: 1
---

# Access

Access is provided through a web browser:

![Login Page](/img/nethcti/Pagina_Login.png)

The connection link and login credentials are specific to your installation and are provided during the initial setup phase.

## Requirements {#requirements}

- A modern web browser (Chrome, Firefox, or Edge)
- Active internet connection
- Valid NethVoice account
- Access to your organization's NethVoice server

## Login Steps {#login-steps}

1. Open your web browser
2. Navigate to your NethVoice CTI URL (provided by your administrator)
3. Enter your username and password
4. Click the login button
5. You will be redirected to the main interface

## Two-Factor Authentication (2FA) {#two-factor-authentication}

Two-factor authentication (2FA) provides an additional layer of security for your NethVoice CTI account by requiring a second verification method during login.

### Enabling 2FA

1. Go to **Settings** → **Authentication**
2. Look for the "Two-Factor Authentication" section showing the current status (enabled or disabled)
3. Click the configuration button to begin setup
4. Choose your setup method:
   - **QR Code**: Scan the QR code with your authenticator app (e.g., Google Authenticator)
   - **Secret Key**: Manually enter the secret code into your authenticator app
5. Enter the OTP (one-time password) code from your authenticator
6. Click confirm
7. You will see a confirmation message when 2FA is successfully enabled

### Recovery Codes

When 2FA is enabled, you can access your recovery codes in Settings (password verification required). These codes are:

- **Single-use**: Each code can only be used once
- **Automatic regeneration**: When all codes are used, new ones are automatically generated
- **Emergency access**: Use these codes if you lose access to your authenticator app

### Logging In with 2FA

When 2FA is enabled:

1. Enter your username and password as usual
2. You will be prompted to enter your OTP code
3. Open your authenticator app and enter the 6-digit code
4. You will be logged in successfully

### Disabling 2FA

To turn off two-factor authentication:

1. Go to **Settings** → **Authentication**
2. Click the configuration button
3. Enter your password to confirm
4. 2FA will be disabled
5. You will be logged out from all active sessions for your account

### Supported Authenticator Apps

2FA works with any standard OTP (one-time password) authenticator. Tested and confirmed working apps include:

- **Google Authenticator** (all platforms)
- **Bitwarden** (password manager with 2FA support)
- Any other OTP-compliant authenticator app
