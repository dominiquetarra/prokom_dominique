glossary = {
    'variable' : 'nama yang menyimpan nilai' , 
    'integer' : 'bilangan bulat' , 
    'float' : 'bilangan desimal' , 
    'loop' : 'pengulangan perintah' , 
    'list' : 'daftar urutan' ,
    'key' : 'label data' , 
    'value' : 'isi data dalam key' , 
    'string' : 'karakter dalam tanda kutip' ,
    'dictionary' : 'kumpulan data dalam bentuk key dan value' , 
    'comment' : 'catatan yang diabaikan Python'
}
for kata, arti in glossary.items() :
    print(f"{kata.title()} : {arti}")
