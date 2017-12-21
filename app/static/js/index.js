var divTooltip = $("<div></div>");
divTooltip.addClass("tooltip fade left in");
divTooltip.css("display","block");

var divArrow = $("<div></div>");
divArrow.addClass("tooltip-arrow");

var divInner = $("<div></div>");
divInner.addClass("tooltip-inner");



$(document).ready(function(){

    $("i.es-icon-edit").mouseover(function(){
        $("div.es-bar").append(divTooltip.append(divArrow).append(divInner.text('我的考试/作业')).css({"top":"228px","left":"-101px"}));
    }).mouseout(function(){
        $("div.es-bar").children().last().remove();
    });

    $("i.es-icon-book").mouseover(function(){
        $("div.es-bar").append(divTooltip.append(divArrow).append(divInner.text('我的课程/班级')).css({"top":"272px","left":"-101px"}));
    }).mouseout(function(){
        $("div.es-bar").children().last().remove();
    });
    $("i.es-icon-notifications").mouseover(function(){
        $("div.es-bar").append(divTooltip.append(divArrow).append(divInner.text('通知')).css({"top":"316px","left":"-50px"}));
    }).mouseout(function(){
        $("div.es-bar").children().last().remove();
    });
    // $("i.es-icon-qq").mouseover(function(){
    //     alert("qq")
    // });
    $("li.bar-qq-btn").mouseover(function(){

    })
    $("i.es-icon-phone").mouseover(function(){
        alert("电话")
    });
    $("i.es-icon-weixin").mouseover(function(){
        alert("微信")
    });


})
