
const CreateButton = document.getElementById('createUrl')
const GetListButton = document.getElementById('getList')




function sendUrl() {
    var linkUrl = $('#url_field');
    var dateDuration = $('#expireAt')
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
                linkUrl.next().append(data.errors.url);
                dateDuration.next().append(data.errors.expireAt);
            }
        },
        errors: (errors) => {
            console.log(errors)
        },
    })
}


function getList() {
    $.ajax({
        url: ShortenerLink,
        type: 'get',
        data: {
        },
        success: (data) => {
            console.log(data)
            if (data.list_urls) {
                var answerBlock = $('#answer');
                answerBlock.empty();
                answerBlock.append(
                    '<label for="expireAt">Вот и Ваша ссылка:</label>',
                    '<input type="text" class="form-control" value="' + data.short_url + '">'
                );
            } else if (data.errors) {
                linkUrl.empty();
                dateDuration.empty();
                linkUrl.next().append(data.errors.url);
                dateDuration.next().append(data.errors.expireAt);
            }
        },
        errors: (errors) => {
            console.log(errors)
        },
    })
}

CreateButton.addEventListener('click', sendUrl)
GetListButton.addEventListener('click', getList)


