
$(document).ready(function(){
    if(localStorage.getItem("lang") === null){
        setTimeout(() => {
            $("#langFr").click()
            $("#langFr").addClass('activeli')
        }, 500);
    }
    else{
        if(localStorage.getItem("lang") == 'en'){
            setTimeout(() => {
                $("#langEn").click()
                $("#langEn").addClass('activeli')
            }, 500);
        }
        else{
            setTimeout(() => {
                $("#langFr").click()
                $("#langFr").addClass('activeli')
            }, 500);
        }
    }
    // localStorage.setItem("admin_token",response['token']);
})

$("#langFr").click(function(){
    localStorage.setItem("lang",'fr');
    $("#langFr").addClass('activeli');
    $("#langEn").removeClass('activeli');
});


$("#langEn").click(function(){
    localStorage.setItem("lang",'en');
    $("#langEn").addClass('activeli');
    $("#langFr").removeClass('activeli');



});

//  $(document).ready(function(){
//      setTimeout(() => {
//          $("#langFr").click()
//      }, 500);
//  })
var currentLocation = window.location.pathname;
if (currentLocation == '/about/') {
    $("#aboutUs").addClass('activeli')
    banners('about')
}
else if (currentLocation == '/gallery/') {
    $("#gallery").addClass('activeli')
    banners('gallery')
}
else if (currentLocation == '/blog/') {
    $("#blog").addClass('activeli')
    banners('blog')
}
else if (currentLocation == '/contact/') {
    $("#contactLi").addClass('activeli')
    banners('contact')
}
else if(currentLocation == '/'){
    $("#home").addClass('activeli')
    $("#product").removeClass('activeli')
    $("#contact").removeClass('activeli')
    banners('home')
}

$(document).ready(function () {
    $('.claimedRight').each(function (f) {
        var newstr = $(this).text().substring(0, 100);
        $(this).text(newstr);

    });
})

$("#home").click(function(){
    $(this).addClass('activeli')
    $("#contactLi").removeClass('activeli')
    $("#products").removeClass('activeli')
})

$("#contactLi").click(function(){
    $(this).addClass('activeli')
    $("#home").removeClass('activeli')
    $("#products").removeClass('activeli')
    $("#blog").removeClass('activeli')
    $("#gallery").removeClass('activeli')
    $("#aboutUs").removeClass('activeli')
});

$("#products").click(function(){
    $(this).addClass('activeli')
    $("#home").removeClass('activeli')
    $("#contactLi").removeClass('activeli')
    $("#blog").removeClass('activeli')
    $("#gallery").removeClass('activeli')
    $("#aboutUs").removeClass('activeli')
});

$(document).ready(function(){
    if ($(window).width() <= 768) {
        $("#langDiv").removeClass('lang')
        $("#langDiv").addClass('lang-mob')
     }
     else {
         $("#langDiv").removeClass('lang-mob')
        $("#langDiv").addClass('lang')
     }
})

$("#contcactForm").submit(function(){
    swal("Success!", "We will get back to you soon!", "success")    
});


function banners(category){
    var csrf_token = $("input[name=csrfmiddlewaretoken]").val();
    data={
        'category':category,
        csrfmiddlewaretoken:csrf_token
    }
    $.ajax({
        url:"/banner/",
        type:"POST",
        data:data,
        success:function(response){
            $("#bannerHeader").html(response['heading_1'])
            $("#bannerContent").html(response['heading_2'])
        }
    })
}