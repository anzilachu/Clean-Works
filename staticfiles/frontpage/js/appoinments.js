$(document).ready(function(){
    $('#department , #clinic').on('change' , function(){

        var department = $('#department').val()
        var clinic = $('#clinic').val()
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

        $.ajax({
            type: 'POST',
            url: '/get-doctors/',
            data: {
                'department':department,
                'clinic':clinic,
                'csrfmiddlewaretoken': csrftoken,
            },
            success: function (response) {
                $('#doctor-select').html(response.data)
            },
            error: function () {
            }
        });
    })

    
    $('#appoinment-btn').on('click', function () {
        console.log("Clicked!");
    
        var name = $('#name').val();
        var contact = $('#contact').val();
        var date = $('#date').val();
        var clinic = $('#clinic').val();
        var department = $('#department').val();
        
        // Check the class selector
        var selectedDoctorElement = $('.option.selected.doctorvd');
        console.log("Selected Doctor Element:", selectedDoctorElement);
    
        // Check the data attribute
        var selectedDoctorId = String(selectedDoctorElement.data('value'));
        console.log("Selected Doctor ID:", selectedDoctorId);
    
        console.log("Data:", { 'name': name, 'contact': contact, 'date': date, 'clinic': clinic, 'department': department, 'doctor': selectedDoctorId });
    
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    
        $.ajax({
            type: 'POST',
            url: '/appoinment/',
            data: {
                'name': name, 'contact': contact, 'date': date, 'clinic': clinic, 'department': department, 'doctor': selectedDoctorId, 'csrfmiddlewaretoken': csrftoken
            },
            success: function (response) {
                $('#aform')[0].reset();
                $('#response').append('<div class="alert alert-success alert-dismissible fade show" role="alert"> Your Appointment Booked Successfully !! </div>');
                console.log("Success:", response);
            },
            error: function () {
                $('#response').append('<div class="alert alert-danger alert-dismissible fade show" role="alert"> An error occurred </div>');
                console.log("Error!");
            }
        });
    });
    
});
    

    


