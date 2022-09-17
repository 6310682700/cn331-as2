# cn331-as2

ณนฐ์ อังสุวพัฒนากุล 6310682700  
กฤตกร ชัยรัตนารมย์  6310682692  

[Video สาธิต](https://drive.google.com/file/d/16REoCU497_hNT3W1QoCigcOYMSXUZth9/view?usp=sharing)  

```bash
$ # Get the code
$ git clone https://github.com/6310682700/cn331-as2.git
$ cd cn331-as2
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Change Directory to work directory
$ # cd reg_site
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```
Link สำรอง https://drive.google.com/file/d/16REoCU497_hNT3W1QoCigcOYMSXUZth9/view?usp=sharing  

#Function:  
1. Login รับค่า username และ password เพื่อนำไปใช้ในการ authentication  
2. Logout ทิ้งค่า username และ password  
3. search ค้นหารายวิชาเพื่อลงทะเบียน  
4. enroll เก็บข้อมูลรายวิชาแล้วนำไปใส่ใน database  
5. remove_enroll เอาข้อมูรายวิชาออกจาก database  
6. capacity เพิ่ม ลบจำนวนที่นังในวิชานั้นๆตามจำนวนคนลงทะเบียน  
7. status admin สามารถเปิด-ปิดรับวิชาได้  
8. sidebar เปิด-ปิดได้  
