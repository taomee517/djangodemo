from project.carbrand.models import Brand, Series
# Create your tests here.
import django
django.setup()


if __name__ == '__main__':
    brand = Brand()
    brand.brand_name = 'Auqi'
    brand.state = 'Germany'
    brand.logo_url = 'http://img.chebiaow.com/thumb/cb/allimg/1303/1-1303061Z600520,c_fill,h_138,w_160.jpg'
    brand.is_deleted = False
    brand.save()
