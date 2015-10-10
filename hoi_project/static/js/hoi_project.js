$('#id_fecha_nacimiento').datepicker({
onSelect: function (value, ui) {
    var today = new Date();
    var format = value.split("/");
    var dob = new Date(format[2], format[1], format[0]);
    var diff = (today - dob);
    var age = Math.floor(diff / 31536000000);
    $('#id_edad').text(age);
},
dateFormat: 'dd/mm/yy',
maxDate: '+0d',
yearRange: '1920:2010',
changeMonth: true,
changeYear: true
});
