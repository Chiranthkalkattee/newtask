fetch('http://127.0.0.1:8000/candidate/')
.then(res=>res.json())
.then(data=>getdata(data))

function getdata(data){
    console.log(data)
}
