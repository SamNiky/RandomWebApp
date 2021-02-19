$(document).ready(function(){
    $('#id_username').removeAttr('autofocus');
    $('#id_username').attr('placeholder', "придумайте логин");
    $('#id_password1').attr('placeholder', "придумайте пароль");
    $('#id_password2').attr('placeholder', "повторите пароль");
    $('.alert').hide();
    $('.btn-form').attr('type', 'button');

    $('#id_username').focusout(function(){
        login = $(this).val()
        if (login == 0){
            $('.login-a').hide();
        }else{
            let logreg = regexp = /[0-9A-Za-z]{4,149}/
            answer = logreg.test(login)
            if (answer == true){
                $('.login-a').hide();
            }else{
                $('.login-a').text("логин должен быть не менее 4 символов из букв или цифр");
                $('.login-a').show();
            }
        }
    });

    $('#id_password1').focusout(function(){
        pass1 = $(this).val()
        if (pass1 == 0){
            $('.pass1-a').hide();
        }else{
            let passreg = regexp = /(?=.*[A-Za-z])[0-9A-Za-z@.+-_ ]{8,50}/
            answer = passreg.test(pass1)
            if (answer == true){
                $('.pass1-a').hide();
            }else{
                $('.pass1-a').text("допустимые символы (@.+-_) должен иметь минимум 1 букву");
                $('.pass1-a').show();
            }
        }
    });


    setInterval(function(){
        password1 = $('#id_password1').val()
        password2 = $('#id_password2').val()
        display = $('.pass2-a').css('display')
        if(password1 != password2){
           $('.pass2-a').text("пароли не совпадают");
           $('.pass2-a').show();
        }else{
            $('.pass2-a').hide();
        }
        display = $('.alert').css('display');
        if(display == 'none'){
           $('.btn-form').attr('type', 'submit');
        }
    }, 250);

//AJAX request
    $('#id_username').focusout(function(){
        $.ajax({
            url: '/sign-up',
            type: 'get',
            data: {
                user_name: $(this).val()
            },
            success: function(response){
                if(response.ans == 1){
                    $('.login-b').text("логин занят");
                    $('.login-b').show();
                }else{
                    $('.login-b').hide();
                }
            }
        });
    });
});