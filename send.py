from pushover import Client

user  = 'u88o975vp68jt3gaoyhfny9uq4cp4c'
token = 'ar3tggesdyxaaz7beq1wxwftscshsk'

def alert(text, **kwargs):
    """
    >>> alert("Doctest",title="Title", sound="magic",url="https://school4one.com/",attachment=open("sample.png","rb"),url_title="School 4 One Link")
    'OK'
    """
    client = Client(user, api_token=token)
    client.send_message(text, html=1 , **kwargs)
    return 'OK'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
