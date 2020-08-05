$(function(){

    $('.slider__inner').slick({
        nextArrow: '<button type="button" class="slick-btn slick-next"><img src="img/arrowr.png" alt=""></button>',
        prevArrow: '<button type="button" class="slick-btn slick-prev"><img src="img/arrowl.png" alt=""></button>',
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 6000,  
    
    });
    document.getElementById('descr').hidden = false;
    document.getElementById('cast').hidden = true;
    document.getElementById('thrl').hidden = true;
    document.getElementById('photo').hidden = true;
    document.getElementById('descr-btn').style.cssText=`background-color: black; color: wheat; border:2px solid black`;
    document.getElementById('cast-btn').style.cssText=`background-color:""; color:""`;
    document.getElementById('thrl-btn').style.cssText=`background-color:""; color:""`;
    document.getElementById('photo-btn').style.cssText=`background-color:""; color:""`;
    
    document.getElementById('descr-btn').onclick = function() {
        document.getElementById('descr').hidden = false;
        document.getElementById('cast').hidden = true;
        document.getElementById('thrl').hidden = true;
        document.getElementById('photo').hidden = true;
        document.getElementById('descr-btn').style.cssText=`background-color: black; color: wheat; border:2px solid black`;
        document.getElementById('cast-btn').style.cssText=`background-color:""; color:""`;
        document.getElementById('thrl-btn').style.cssText=`background-color:""; color:""`;
        document.getElementById('photo-btn').style.cssText=`background-color:""; color:""`;
      }
    document.getElementById('cast-btn').onclick = function() {
        document.getElementById('descr').hidden = true;
        document.getElementById('cast').hidden = false;
        document.getElementById('thrl').hidden = true;
        document.getElementById('photo').hidden = true;
        document.getElementById('descr-btn').style.cssText=`background-color:""; color:""`;
        document.getElementById('cast-btn').style.cssText=`background-color: black; color: wheat; border:2px solid black`;
        document.getElementById('thrl-btn').style.cssText=`background-color:""; color:""`;
        document.getElementById('photo-btn').style.cssText=`background-color:""; color:""`;
        }
    document.getElementById('thrl-btn').onclick = function() {
        document.getElementById('descr').hidden = true;
        document.getElementById('cast').hidden = true;
        document.getElementById('thrl').hidden = false;
        document.getElementById('photo').hidden = true;
        document.getElementById('descr-btn').style.cssText=`background-color:""; color:""`;
        document.getElementById('cast-btn').style.cssText=`background-color:""; color:""`;
        document.getElementById('thrl-btn').style.cssText=`background-color: black; color: wheat; border:2px solid black`;
        document.getElementById('photo-btn').style.cssText=`background-color:""; color:""`;
        }
    document.getElementById('photo-btn').onclick = function() {
        document.getElementById('descr').hidden = true;
        document.getElementById('cast').hidden = true;
        document.getElementById('thrl').hidden = true;
        document.getElementById('photo').hidden = false;
        document.getElementById('descr-btn').style.cssText=`background-color:""; color:""`;
        document.getElementById('cast-btn').style.cssText=`background-color:""; color:""`;
        document.getElementById('thrl-btn').style.cssText=`background-color:""; color:""`;
        document.getElementById('photo-btn').style.cssText=`background-color: black; color: wheat; border:2px solid black;`;
        }
      
    
        $('.slider__cast').slick({
            
            nextArrow: '<button type="button" class="actors-slick-btn actors-slick-next"><img src="img/arrowr.png" alt=""></button>',
            prevArrow: '<button type="button" class="actors-slick-btn actors-slick-prev"><img src="img/arrowl.png" alt=""></button>',
            slidesToShow: 4,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 3000,
        
        
        });
    })

    