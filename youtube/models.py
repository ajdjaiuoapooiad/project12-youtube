from django.db import models

class Category(models.Model):
    name=models.CharField('カテゴリー名',max_length=20)
    created_at=models.DateTimeField('作成日',auto_now_add=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField('タイトル',max_length=100)
    text=models.TextField('説明文')
    thumbnail=models.ImageField('サムネイル(空欄可)',upload_to='media/thumbnails/',null=True,blank=True)
    movie=models.FileField('動画',upload_to='uploads/%Y/%m/%d/')
    created_at=models.DateTimeField('作成日',auto_now_add=True)
    updated_at=models.DateTimeField('更新日',auto_now=True)
    category=models.ForeignKey(Category,verbose_name='カテゴリー',on_delete=models.PROTECT,null=True)
    
    def __str__(self):
        return self.title
    