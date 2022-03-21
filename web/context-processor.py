from . models import banner,background_image,social_media,CompanyDetail,CheckProcess

def main_context(request):
    baner = banner.objects.all().first()
    images = background_image.objects.all().first()
    company_deatils =CompanyDetail.objects.all().order_by("-id")
    check_process=CheckProcess.objects.all().order_by("-id")[:1]    
    facebook = ''
    instagramme = ''
    snapchat = ''
    twiter = ''
    youtube = ''
    try:
        social_medias = social_media.objects.all()
        for i in social_medias:
            if i.social_media == 'facebook':
                facebook = i.link
            elif i.social_media == 'instagramme':
                instagramme = i.link
            elif i.social_media == 'snapchat':
                snapchat = i.link
            elif i.social_media == 'twiter':
                twiter = i.link
            elif i.social_media == 'youtube':
                youtube = i.link
    except Exception as e:
        pass
    return {
        'domain' : request.META['HTTP_HOST'],
        'banner'  : baner,
        'images': images,
        'twiter':twiter,
        'facebook':facebook,
        'instagramme':instagramme,
        'snapchat':snapchat,
        'youtube':youtube, 
        'company_deatils':company_deatils,
        "check_process":check_process
       
    }