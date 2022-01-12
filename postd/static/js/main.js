
let MyHeader = (function(){
    let HeaderFunction = function(){
        const lostjq = $("#lost")
        const lost1jq = $("#lost1")
        const headlink = document.querySelectorAll('.header-link')

        $(window).resize(function () { 
            let window_size=window.innerWidth
            if (window_size>768){
                lostjq.css({display:'flex'})
                lost1jq.css({display:'flex'})
            }else{
                lostjq.css({display:'none'})
                lost1jq.css({display:'none'})
            }
        });
        $('#bar-icon').click(function(){
            lostjq.slideToggle(400,function(){
                lost1jq.slideToggle(400);
            });
        })
        const headerjq = $("header")
        let window_size=window.innerWidth
        if (window_size<768){
            lostjq.css({display:'none'})
            lost1jq.css({display:'none'})
            headerjq.css({
                backgroundColor:'#f1f1f1',
                boxShadow:'0 0 15px 0 rgba(78, 78, 78, 0.342)'
            })
            $(headlink[0]).css({color:'#000'})
            for(i=1;i<=headlink.length;i++){
                $(headlink[i]).css({color:"rgba(63, 59, 59,0.83)"})
            }
        }
    
        window.addEventListener('scroll',()=>{
            if (document.documentElement.scrollTop<=50){
                headerjq.css({
                    backgroundColor:'transparent',
                    boxShadow:'0 0 0 0 blue'
                })
                for(i=0;i<=headlink.length;i++){
                    $(headlink[i]).css({
                        color:'#fff'
                    });
                }
            }else{
                headerjq.css({
                    backgroundColor:'#f1f1f1',
                    boxShadow:'0 0 15px 0 rgba(78, 78, 78, 0.342)'
                })
                $(headlink[0]).css({color:'#000'})
                for(i=1;i<=headlink.length;i++){
                    $(headlink[i]).css({
                        color:'#3f3b3b'
                    });
                }
            }
        })
    
    }

    return { header : HeaderFunction}

})()




MyHeader.header()


$(document).ready(function () {
    var jazzMusic = document.getElementById("music");
    jazzMusic.play();
});

