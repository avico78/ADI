from .worket import app

# tasks.py
@app.task(bind=True, name='refresh')  
def refresh(self, urls):  
  for url in urls:  
    fetch_source.s(url).delay() 

@app.task(bind=True, name='fetch_source')  
def fetch_source(self, url):  
  source = newspaper.build(url)  
  for article in source.articles:  
    fetch_article.s(article.url).delay()

# tasks.py
@app.task(bind=True, name='save_article', queue='minio')
def save_article(self, bucket, key, text):  
  minio_client = Minio('localhost:9000',
    access_key='AKIAIOSFODNN7EXAMPLE',
    secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    secure=False)  
  try:  
    minio_client.make_bucket(bucket, location="us-east-1")  
  except BucketAlreadyExists:  
    pass  
  except BucketAlreadyOwnedByYou:  
    pass  

  hexdigest = hashlib.md5(text.encode()).hexdigest()

  try:
    st = minio_client.stat_object(bucket, key)  
    update = st.etag != hexdigest  
  except NoSuchKey as err:  
    update = True  

  if update:  
    stream = BytesIO(text.encode())  
    minio_client.put_object(bucket, key, stream, stream.getbuffer().nbytes)  
