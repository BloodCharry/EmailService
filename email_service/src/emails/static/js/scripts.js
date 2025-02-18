$(document).ready(function () {
  $('#campaignForm').on('submit', function (e) {
    e.preventDefault(); // Предотвращаем отправку формы

    const subject = $('#id_subject').val();
    const htmlTemplate = $('#id_html_template').val();

    if (!subject || !htmlTemplate) {
      alert('Пожалуйста, заполните все поля.');
      return;
    }

    // Отправляем форму через AJAX
    $.ajax({
      url: '/create-campaign/',
      method: 'POST',
      data: $(this).serialize(),
      success: function (response) {
        alert('Рассылка успешно создана!');
        $('#campaignModal').modal('hide'); // Закрываем модальное окно
      },
      error: function () {
        alert('Произошла ошибка при создании рассылки.');
      }
    });
  });
});