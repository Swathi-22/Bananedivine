
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
    $("#bannerHeader").html(' À PROPOS DE NOUS')
    $("#bannerContent").html('Ressentez le vrai goût de la banane')

}
else if (currentLocation == '/gallery/') {
    $("#gallery").addClass('activeli')
    $("#bannerHeader").html('Gallery')
    $("#bannerContent").html('Évolution Banane Plantain')
}
else if (currentLocation == '/blog/') {
    $("#blog").addClass('activeli')
    $("#bannerHeader").html('Blog')
    $("#bannerContent").html('Get updated with our latest news and blogs')
}
else if (currentLocation == '/contact/') {
    $("#contactLi").addClass('activeli')
    $("#bannerHeader").html('Contact')
    $("#bannerContent").html('')
}
else if(currentLocation == '/'){
    $("#home").addClass('activeli')
    $("#product").removeClass('activeli')
    $("#contact").removeClass('activeli')
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

