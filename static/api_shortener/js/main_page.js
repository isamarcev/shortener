
const CreateButton = document.getElementById('createUrl')
const GetListButton = document.getElementById('getList')




function sendUrl() {
    var linkUrl = $('#url_field');
    var dateDuration = $('#expireAt');
    var doesNotExists = $('.does-not-exists');
    doesNotExists.css('display', 'none')
    var errorUrl = $('.error-message-url');
    errorUrl.empty()
    var errorDate = $('.error-message-date');
    errorDate.empty()
    $.ajax({
        url: ShortenerLink,
        type: 'post',
        data: {
            'url': linkUrl.val(),
            'expireAt': dateDuration.val()
        },
        success: (data) => {
            console.log(data)
            if (data.short_url) {
                var answerBlock = $('#answer');
                answerBlock.empty();
                answerBlock.append(
                    '<label for="expireAt">Вот и Ваша ссылка:</label>',
                    '<input type="text" class="form-control" value="' + data.short_url + '">'
                );
            } else if (data.errors) {
                linkUrl.empty();
                dateDuration.empty();
                errorUrl.append(data.errors.url);
                errorDate.append(data.errors.expireAt);
            }
        },
        errors: (errors) => {
            console.log(errors)
        },
    })
}

var TableBody = $('tbody')

function getList() {
    var tableLink = $('#all-link');
    TableBody.empty()
    $.ajax({
        url: ShortenerLink,
        type: 'get',
        data: {
        },
        success: (data) => {
            if (data) {
                $(data).each(function (index, value) {
                        tableLink.append(
                            '<tr><td>'+ value.url +'</td><td>'+ document.location.origin + '/' + value.key +'</td><td>'+ value.counter +'</td></tr>'
                        )
                    })
                tableLink.css('display', 'table')
            } else {
                alert("Вы еще не создали ни одной ссылки.")
            }

        },
        errors: (errors) => {
            console.log(errors)
        },
    })
}

CreateButton.addEventListener('click', sendUrl)
GetListButton.addEventListener('click', getList)


