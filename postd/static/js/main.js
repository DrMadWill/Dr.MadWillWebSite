let a,
b,
c;
a= true;
d=document.getElementById("lost"); 
c=document.getElementById('lost1');

const header=document.querySelector('header')
header.style.backgroundColor='transparent'
header.style.boxShadow='0 0 0 0 blue'
const headlink = document.querySelectorAll('.header-link')


let m
m=window.innerWidth


if (m<768){
    d.style.display='none'
    c.style.display='none'
    header.style.backgroundColor='#f1f1f1'
    headlink[0].style.color="#000"
    for(i=1;i<=headlink.length;i++){
            headlink[i].style.color="rgba(63, 59, 59,0.83)"
    }
}

// ekran ölçüləri dəyişdikdə dispeyin flex olma hali 

function will(){
    let f

    f=window.innerWidth

    if (f>768){
        d.style.display='flex'
        c.style.display='flex'

        
        
    }else{
        d.style.display='none'
        c.style.display='none'
        
    }

    


}



function iconclick(){
    
    if (a===true){
        
        a=false;
        d.style.display='flex'
        c.style.display='flex'
        
    }else{
        a=true;
        d.style.display='none'
        c.style.display='none'
        

    }
}



// header --> stiky navbar 

window.addEventListener('scroll',()=>{
    if (document.documentElement.scrollTop<=50){
        header.style.backgroundColor='transparent'
        header.style.boxShadow='0 0 0 0 blue'
        
        for(i=0;i<=headlink.length;i++){
            headlink[i].style.color='#fff'
        }
    }else{
        
        header.style.backgroundColor='#f1f1f1'
        headlink[0].style.color='#000'
        header.style.boxShadow='0 0 15px 0 rgba(78, 78, 78, 0.342)'
        for(i=1;i<=headlink.length;i++){
            headlink[i].style.color='#3f3b3b'
            
        }
        
    }
})


// Show More --> btn


// Deskop Show More --> btn

let showBoxDeskop = document.getElementById('showbox');
let btnShowDeskop = document.getElementById('btnDeskop')

function showMore(){
    if (a===true){
        a=false;
        showBoxDeskop.style.display='flex';
        btnShowDeskop.innerHTML='...Show Less';


    }else{
        a=true;
        showBoxDeskop.style.display='none';
        btnShowDeskop.innerHTML='Show More...';
    }


}




// Tablet Show More --> btn

let BoxTablet = document.getElementById('showBoxTablet')
let btnTablet = document.getElementById('btnTablet')

function MoreTablet(){
    if(a==true){
        a=false;
        BoxTablet.style.display='flex'
        btnTablet.innerHTML='...Show Less'
    }else{
        a=true;
        BoxTablet.style.display='none';
        btnTablet.innerHTML='Show More...'
    }
    
}






