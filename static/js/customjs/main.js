function showError() {
    $('#submitSignUp').attr('disabled', 'disabled');
    $('#name_status').addClass('validate_data');

}

function removeError() {
    $('#submitSignUp').removeAttr('disabled', 'disabled');
    $('#name_status').removeClass('validate_data');
    $('#name_status').html("");
}
function checkname() {
    var name = document.getElementById("UserName").value;
    if (name) {
        $.ajax({
            type: 'post',
            url: '/api/UsernameList/',
            data: {
                username: name,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function (response) {

                if (response.response === 'ok') {
                    showError();
                    $('#name_status').html(response.message);
                }
                else {

                    removeError();

                }

                return response;
            }
        });
    }
    else {
        removeError();

        return false;
    }
}

function checkPassword() {
    var password = document.getElementById("password").value.trim(' ');
    if (password.length <= 6) {
        showError();
        $('#name_status').html('Minimum character for password is 6.');
    }
    else {
        removeError()
    }

}

function confirmpassword() {
    var password = document.getElementById("password").value.trim(' ');
    var confirm_password = document.getElementById("confirmPassword").value.trim(' ');
    if (password.length !== confirm_password || password.length <= 6) {
        showError();
        $('#name_status').html("Password mismatched. ");
    }
    else {
        removeError()
    }


}

function postNewUser() {
    checkname();
    confirmpassword();
    checkPassword();
}


// -------------------------- setting page school detail ----------------------------------
function getSchoolDetail() {
    $.ajax({
        type: 'get',
        url: '/api/SchoolDetail/',
        success: function (response) {

            $('#SDid').val(response.ID);
            $('#SDschoolName').val(response.SchoolName);
            $('#SDcity').val(response.City);
            $('#SDemail').val(response.Email);
            $('#SDaddress').val(response.Address);
            $('#SDphone').val(response.PhoneNumber);
            $('#SDcountry').val(response.Country);
            $('#SDstate').val(response.State);
            $('#SDpin').val(response.PinCode);
            $('#SDwebsite').val(response.Website);
            $('#imagePreview').css('background-image', 'url(' + response.Logo + ')');
            return response;
        }
    });

}


function PostSchoolDetail() {
    var SDschoolName = $('#SDschoolName').val();
    var SDcity = $('#SDcity').val();
    var SDemail = $('#SDemail').val();
    var SDaddress = $('#SDaddress').val();
    var SDphone = $('#SDphone').val();
    var SDcountry = $('#SDcountry').val();
    var SDstate = $('#SDstate').val();
    var SDpin = $('#SDpin').val();
    var SDwebsite = $('#SDwebsite').val();
    var SDid = $('#SDid').val();
    // var school_name = $('#imagePreview').css('background-image','url(' + response.Logo + ')');

    $.ajax({
        type: 'post',
        url: '/api/PostSchoolDetail/',
        data: {
            SDschoolName: SDschoolName,
            SDcity: SDcity,
            SDemail: SDemail,
            SDaddress: SDaddress,
            SDphone: SDphone,
            SDcountry: SDcountry,
            SDstate: SDstate,
            SDpin: SDpin,
            SDwebsite: SDwebsite,
            SDid: SDid,
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
        },
        success: function (response) {
            if (response.response === 'ok') {

                $('#name_status').addClass('validate_data');
                $('#name_status').html('School Details saved successfully.');
                getSchoolDetail();
                $('#name_status').fadeIn().fadeOut(2000)

            }
            else {
                getSchoolDetail();
                $('#name_status').removeClass('validate_data');
                $('#name_status').fadeIn().fadeOut(2000)

            }

            return response;
        }
    });
}

function uploadSchoolLogo() {
    var imageData = document.getElementById("imageUpload").files[0];
    var form_data = new FormData();
    form_data.append('file', imageData);
    var SDid = $('#SDid').val();
    form_data.append('SDid', SDid);

    $.ajax({
        type: 'post',
        url: '/api/PostSchoolLogo/',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,


        success: function (response) {
            if (response.response === 'ok') {
                $('#name_status').addClass('validate_data');
                $('#name_status').html('Logo changed successfully.');
                getSchoolDetail();
               $('#name_status').fadeIn().fadeOut(2000)
            }
            else {
                getSchoolDetail();
                $('#name_status').removeClass('validate_data');
                $('#name_status').fadeIn().fadeOut(2000)

            }

            return response;
        }
    });


}

function getSchoolSocialLink() {
    $.ajax({
        type: 'get',
        url: '/api/GetSchoolSocialLinks/',
        success: function (response) {

            $('#SLid').val(response.ID);
            $('#SLfacebook').val(response.Facebook);
            $('#SLtwitter').val(response.Twitter);
            $('#SLplaystore').val(response.Playstore);
            return response;
        }
    });

}


function PostSchoolSocialLink() {
    var SLid = $('#SLid').val();
    var SLfacebook = $('#SLfacebook').val();
    var SLtwitter = $('#SLtwitter').val();
    var SLplaystore = $('#SLplaystore').val();

    $.ajax({
        type: 'post',
        url: '/api/PostSchoolSocialLinks/',
        data: {
            SLid: SLid,
            SLfacebook: SLfacebook,
            SLtwitter: SLtwitter,
            SLplaystore: SLplaystore,

            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
        },
        success: function (response) {
            if (response.response === 'ok') {
                $('#name_status').addClass('validate_data');
                $('#name_status').html('School Social Links saved successfully.');
                $('#name_status').fadeIn().fadeOut(2000)
                getSchoolSocialLink();
            }
            else {
                getSchoolSocialLink();
                $('#name_status').removeClass('validate_data');
                $('#name_status').html("");
                $('#name_status').fadeIn().fadeOut(2000)

            }

            return response;
        }
    });
}


function checknameComputerOperator() {
    var name = document.getElementById("UAusername").value;
    if (name) {
        $.ajax({
            type: 'post',
            url: '/api/UsernameList/',
            data: {
                username: name,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function (response) {

                if (response.response === 'ok') {
                    $('#name_status').addClass('validate_data');
                    $('#name_status').html(response.message);
                    $('#AddComputerOperator').attr('disabled', 'disabled');
$('#name_status').fadeIn().fadeOut(2000)                }
                else {

                    $('#name_status').removeClass('validate_data');
                    $('#AddComputerOperator').removeAttr('disabled', 'disabled');
                }

                return response;
            },
            error: function () {
                $('#name_status').addClass('validate_data');
                $('#name_status').html('error.');
                $('#name_status').fadeIn().fadeOut(2000)
            }
        });
    }
    else {
        removeError();

        return false;
    }
}

//--------------------------------Get User(Computer Operator) Detail-----------------------

function userDetailId(id) {
    $.ajax({
        type: 'get',
        url: '/api/GetComputerOperatorDetail/' + id + '',
        success: function (context) {
            $("#imagepic").attr("src", context.opImage);
            $("#opname").text(context.name);
            $("#opnamehead").text(context.name + ' Detail');
            $("#opqualification").text(context.qualification);
            $("#opemail").text(context.email);
            $("#mno").text(context.mobileno);
            $("#dob").text(context.dob);
            $("#doj").text(context.doj);
            $("#aadhar").text(context.aadhar);
            $("#tadd").text(context.taddress);
            $("#padd").text(context.paddress);
        }
    });
}
//-------------------------------------Edit User(Computer Operator) Detail ----------------

//-------------------------------------
function PostSchoolSession() {
    var session = document.getElementById("Session").value;

    if (session !=="") {
        $.ajax({
            type: 'post',
            url: '/api/PostSession/',
            data: {
                Session: session,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function (response) {
                if (response.response === 'ok') {
                    $('#name_status').addClass('validate_data');
                    $('#name_status').html('Session Successfully Added');
                    $('#sessionID').append('<li><strong>' + session + '</strong></li>');
                    $('#name_status').fadeIn().fadeOut(2000)

                }
                else {

                    $('#name_status').addClass('validate_data');
                    $('#name_status').html('Error. Please Try Again.');
                    $('#name_status').fadeIn().fadeOut(2000)
                }
            }
        });
    }
    else {
        $('#name_status').addClass('validate_data');
        $('#name_status').html('Session Required');
        $('#name_status').fadeIn().fadeOut(2000)
    }
}


function getSessionList() {
    $.ajax({
        type: 'get',
        url: '/api/GetSession/',
        success: function (response) {
            for (i in response) {
                var listSession = '<li><strong>' + response[i].Session + '</strong></li>';
                $('#sessionID').append(listSession);
            }
            return response;
        },
        error: function () {
            $('#name_status').addClass('validate_data');
            $('#name_status').html('error.');
            $('#name_status').fadeIn().fadeOut(2000)
        }
    });

}




// -------------------------------------Student--------------------------

