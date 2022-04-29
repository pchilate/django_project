from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

from django.core.validators import MaxValueValidator,MinValueValidator




#choices for Laptops

title_lappy = [
   ('Dell', 'Dell'),
   ('HP', 'HP'),
   ('Lenovo', 'Lenovo'),
   ('ASUS', 'ASUS'),
   ('Acer', 'Acer'),
   ('Apple', 'Apple'),
]

Uses_lappy = [
   ('Home', 'Home'),
   ('Business', 'Business'),
   ('Gaming','Gaming'),
   ('Student', 'Student'),
   ('Premium', 'Premium')
]

size = [
  (13.0, 13.0 ),
  (13.3,13.3),
  (14.0,14.0),
  (14.5,14.5),
  (15.0,15.0),
  (15.6,15.6)
]

memo_type = [
    ('DDR4','DDR4'),
    ('DDR3', 'DDR3')
]

maxi_memo = [
    (32,32),
    (16,16),
    (12,12),
    (8,8),
    (4,4)
]

hard_disk = [
   ('HDD','HDD'),
   ('SSD','SSD'),
   ('HDD+SSD', 'HDD+SSD')
]



Resolution_lappy = [
    ('1366 x 768','1366 x 768'),
    ('1600 x 900','1600 x 900'),
    ('1920 x 1080','1920 x 1080'),
    ('2304×1440','2304×1440')
]

Processor_Type = [
   ('AMD-Series','AMD-Series'),
   ('CORE i3', 'CORE i3'),
   ('CORE i5', 'CORE i5'),
   ('CORE i7', 'CORE i7'),
]

os = [
   ('Windows 11 Homes' , 'Windows 11 Homes'),
   ('Windows 10' , 'Windows 10'),
   ('Linux', 'Linux'),
   ('Mac OS','Mac OS')
]

b_life = [
     (15,15),
     (12,12),
     (10,10),
     (8,8),
     (4,4),
]

#model for laptops

class Laptops(models.Model):
    LID = models.IntegerField(primary_key = True)
    Title = models.CharField( max_length = 20,choices = title_lappy)
    Description = models.TextField()
    Series = models.CharField(max_length = 50)
    Brand = models.CharField(max_length = 50, choices = title_lappy)
    Uses = models.CharField( max_length = 50, choices  = Uses_lappy)
    Screen_size = models.FloatField(choices = size)
    Price = models.DecimalField(max_digits=11, decimal_places=2)
    Memory_Type = models.CharField(max_length = 10 , choices = memo_type)
    Maximum_memory = models.IntegerField(choices = maxi_memo)
    Hard_Disk_Description = models.CharField(max_length = 10, choices = hard_disk)
    Hard_drive_size = models.IntegerField(null = True)
    Graphic_Card_Description = models.CharField(max_length = 50)
    USB_3_port = models.IntegerField(default = 2)
    USB_2_port = models.IntegerField(default = 1)
    HDMI_Port = models.IntegerField(default = 1)
    Resolution = models.CharField(max_length = 25 , choices = Resolution_lappy)
    Processor_Type  = models.CharField(max_length = 20, choices = Processor_Type)
    Processor_Speed  = models.FloatField()
    Audio_Details = models.CharField(max_length = 30,default = 'Speakers , Headphones')
    Operating_System = models.CharField(max_length = 30, choices = os)
    Battery_life = models.IntegerField(choices = b_life)
    Connectivity_Type =  models.CharField(max_length = 20, default = 'Bluetooth , Wi-Fi')
    Included_components =  models.CharField(max_length = 80, default = '‎Laptop, Power adapter, User guide, Waranty documents')
    Country = models.CharField(max_length = 10)
    Manufacturer = models.CharField(max_length = 10)
    Weight = models.FloatField()
    seller = models.CharField(max_length = 25)
    Image = models.ImageField(upload_to = 'pics/laptops', null = True)



    def __str__(self):
        return self.Title


#choices for monitors

title_mon = [
  ('Samsung','Samsung'),
  ('LG','LG'),
  ('Dell','Dell'),
  ('Lenovo','Lenovo'),
  ('HP','HP'),
  ('Acer','Acer')
]

Uses_mon = [
   ('Home', 'Home'),
   ('Business', 'Business'),
   ('Gaming','Gaming')
]

refresh_rate = [
    (144,144),
    (120,120),
    (90,90),
    (75,75),
    (60,60)
]


display_technology = [
  ('LED','LED'),
  ('LCD','LCD'),
  ('CRT','CRT'),
  ('OLED','OLED'),
  ('QLED','QLED')
]

Resolution_mon = [
('1920 x 1080','1920 x 1080'),
('2560 x 1440','2560 x 1440'),
('3840 x 2160','3840 x 2160'),
('1366 x 768','1366 x 768'),
('1440 x 900','1440 x 900'),
('1280 x 800','1280 x 800'),
('3440 x 1440','3440 x 1440'),
]

Connector_Type = [
     ('DVI','DVI'),
     ('HDMI','HDMI'),
     ('VGA','VGA'),
     ('HDMI+VGA','HDMI+VGA'),
]

# models for monitors

class Monitors(models.Model):
    MID = models.IntegerField(primary_key = True)
    Title = models.CharField( max_length = 20,choices = title_mon)
    Description = models.TextField()
    Series = models.CharField(max_length = 50)
    Brand = models.CharField(max_length = 50, choices = title_mon)
    Uses = models.CharField( max_length = 50, choices  = Uses_mon)
    Screen_size = models.FloatField()
    Price = models.DecimalField(max_digits=11, decimal_places=2)
    Refresh_rate = models.IntegerField(choices = refresh_rate)
    display_technology = models.CharField(max_length = 30, choices = display_technology)
    panel_type = models.CharField(max_length = 50)
    USB_3_port = models.IntegerField(default = 2)
    USB_2_port = models.IntegerField(default = 1)
    Resolution = models.CharField(max_length = 25 , choices = Resolution_mon)
    Connector_Type =  models.CharField(max_length = 20,choices = Connector_Type)
    Country = models.CharField(max_length = 10)
    Manufacturer = models.CharField(max_length = 10)
    Weight = models.FloatField()
    seller = models.CharField(max_length = 25)
    Image = models.ImageField(upload_to = 'pics/monitors', null = True)



    def __str__(self):
        return self.Title



#choices for printers


title_pri = [
   ('cannon','cannon'),
   ('HP','HP'),
   ('EPSON','EPSON')
]

Uses_pri = [
   ('Home/office','Home/office'),
   ('A3 printers','A3 printers'),
   ('Laser printers', 'Laser printers')
]

printer_function = [
   ('print,scan and copy','print,scan and copy'),
   ('pritn only', 'print only')
]

sheet_size = [
  ('A3','A3'),
  ('A4','A4'),
  ('A5','A5'),
  ('A6','A6'),
  ('A3/A4/A5/A6','A3/A4/A5/A6'),
]

Connector_Type_pri = [
   ('USB','USB'),
   ('WiFi','WiFi'),
   ('USB + WiFi','USB + WiFi')
]


# models for printers
class Printers(models.Model):
    PID = models.IntegerField(primary_key = True)
    Title = models.CharField( max_length = 20,choices = title_pri)
    Description = models.TextField()
    Series = models.CharField(max_length = 50)
    Brand = models.CharField(max_length = 50, choices = title_pri)
    Uses = models.CharField( max_length = 50, choices  = Uses_pri)
    Price = models.DecimalField(max_digits=11, decimal_places=2)
    printing_technology = models.CharField(max_length = 30)
    printer_function = models.CharField(max_length = 30, choices = printer_function)
    Operating_System = models.CharField(max_length = 50, default = 'windows')
    printer_output = models.CharField(max_length = 20, default = 'color')
    sheet_size = models.CharField(max_length = 30, choices = sheet_size)
    Connector_Type =  models.CharField(max_length = 20,choices = Connector_Type_pri)
    Country = models.CharField(max_length = 10)
    Manufacturer = models.CharField(max_length = 50)
    Weight = models.FloatField()
    seller = models.CharField(max_length = 25)
    Image = models.ImageField(upload_to = 'pics/printers', null = True)



    def __str__(self):
        return self.Title



#choices for headphonea

title_head = [
   ('JBL','JBL'),
   ('BoAt','BoAt'),
   ('Sony','Sony'),
   ('Realme','Realme'),
   ('Apple','Apple')
]

cat_head = [
   ('Wired','Wired'),
   ('Wireless','Wireless'),
   ('Earbuds','Earbuds')
]

Ear_placement = [
   ('In Ear','In Ear'),
   ('On Ear','On Ear'),
   ('Over Ear','Over Ear')
]


Microphone = [
    ('yes','yes'),
    ('No','No')
]

# models for Headphones
class Headphones(models.Model):
    HID = models.IntegerField(primary_key = True)
    Title = models.CharField( max_length = 20,choices = title_head)
    Description = models.TextField()
    Series = models.CharField(max_length = 50)
    color = models.CharField(max_length = 20)
    Brand = models.CharField(max_length = 50, choices = title_head)
    Category = models.CharField( max_length = 50, choices  = cat_head)
    Price = models.DecimalField(max_digits=11, decimal_places=2)
    Ear_placement = models.CharField(max_length = 20, choices = Ear_placement)
    Microphone = models.CharField(max_length = 10 ,choices = Microphone)
    Connector_Type =  models.CharField(max_length = 20,choices = cat_head)
    Compitible_device = models.CharField(max_length = 40,default = 	'Audio Player , Laptop, Mobile, Tablet')
    Country = models.CharField(max_length = 10)
    Manufacturer = models.CharField(max_length = 50)
    Weight = models.FloatField()
    seller = models.CharField(max_length = 25)
    Image = models.ImageField(upload_to = 'pics/headphones', null = True)



    def __str__(self):
        return self.Title








state_choices = [
("Andhra Pradesh","Andhra Pradesh"),
("Arunachal Pradesh ","Arunachal Pradesh "),
("Assam","Assam"),
("Bihar","Bihar"),
("Chhattisgarh","Chhattisgarh"),
("Goa","Goa"),
("Gujarat","Gujarat"),
("Haryana","Haryana"),
("Himachal Pradesh","Himachal Pradesh"),
("Jammu and Kashmir ","Jammu and Kashmir "),
("Jharkhand","Jharkhand"),
("Karnataka","Karnataka"),
("Kerala","Kerala"),
("Madhya Pradesh","Madhya Pradesh"),
("Maharashtra","Maharashtra"),
("Manipur","Manipur"),
("Meghalaya","Meghalaya"),
("Mizoram","Mizoram"),
("Nagaland","Nagaland"),
("Odisha","Odisha"),
("Punjab","Punjab"),
("Rajasthan","Rajasthan"),
("Sikkim","Sikkim"),
("Tamil Nadu","Tamil Nadu"),
("Telangana","Telangana"),
("Tripura","Tripura"),
("Uttar Pradesh","Uttar Pradesh"),
("Uttarakhand","Uttarakhand"),
("West Bengal","West Bengal"),
("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
("Chandigarh","Chandigarh"),
("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
("Daman and Diu","Daman and Diu"),
("Lakshadweep","Lakshadweep"),
("National Capital Territory of Delhi","National Capital Territory of Delhi"),
("Puducherry","Puducherry")
]

gender = [
  ('Male','Male'),
  ('Female','Female')
]


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    Contact_No = models.IntegerField()
    locality = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    zipcode = models.IntegerField()
    state = models.CharField(max_length = 50, choices = state_choices)

    def __str__(self):
        return str(self.id)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product_id = models.IntegerField()
    category = models.CharField(max_length = 20)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return str(self.id)



status_choices = [
  ('Accepted','Accepted'),
  ('Packed','Packed'),
  ('On the Way','On the Way'),
  ('Delivered','Delivered'),
  ('Cancle','Cancle')
]

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete= models.CASCADE)
    product_id = models.IntegerField()
    category = models.CharField(max_length = 20)
    quantity = models.PositiveIntegerField(default = 1)
    ordered_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 50,choices = status_choices, default = 'Pending')
