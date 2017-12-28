$(document).ready(function(){

    $('.course-item').mouseenter(function(){
        $(this).css("box-shadow","0 5px 5px #888888").offset(function(n,c){
            newPos = new Object();
            newPos.left=c.left-3;
            newPos.top =c.top-3;
            return newPos;
        });
    });
    $('.course-item').mouseleave(function(){
        $(this).css("box-shadow","").offset(function(n,c){
            newPos = new Object();
            newPos.left=c.left+3;
            newPos.top =c.top+3;
            return newPos;
        });
    });
});
