document.getElementById("btnRegister").onclick=function(){
    const mssv=document.getElementById("mssv").value;
    const tensinhvien=document.getElementById("tensinhvien").value;
    const email=document.getElementById("email").value;
    
    const student={
        massinhvien:mssv,
        tensinhvien:tensinhvien,
        emailsinhvien:email,
    }

    localStorage.setItem("sinhvien",JSON.stringify(student))
}


