# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'website_images/{filename}'.format(filename=filename)