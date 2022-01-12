// Show More --> btn

// Show More --> btn
let MyProject = (function(){

    let MainFunction=function(){
        
        // Deskop Show More --> btn
        let isbtnClickDeskop = true
        let btnDeskop=$("#btnDeskop")
        btnDeskop.click(function () { 
            $('#showbox').slideToggle(500,function(){
                if (isbtnClickDeskop===true){
                    isbtnClickDeskop=false;
                    btnDeskop.html('...Show Less');
                }else{
                    isbtnClickDeskop=true;
                    btnDeskop.html('Show More...');
                }
            });
            
        });

        // Tablet Show More --> btn
        let btnTablets = $('#btnTablet')
        let isbtnClickTablet = true
        btnTablets.click(function () { 
            $('#showBoxTablet').slideToggle(500,function(){
                if(isbtnClickTablet==true){
                    isbtnClickTablet=false;
                    btnTablets.html('...Show Less')
                }else{
                    isbtnClickTablet=true;
                    btnTablets.html('Show More...')
                }
            });
        });

    }

    return{
        MainFunction
    }

})()


MyProject.MainFunction()