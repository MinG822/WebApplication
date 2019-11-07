/* 1. <input> 태그 안의 값을 잡는다. */
const inputArea = document.querySelector('#js-userinput')
const button = document.querySelector('#js-go')
const resultArea = document.querySelector('#result-area')

button.addEventListener('click', e => {
    searchAndPush(inputArea.value)
})

inputArea.addEventListener('keydown', e => {
    if (e.keyCode === 13) {
        searchAndPush(inputArea.value)
    }
})

/* 2. Giphy API 를 통해 data 를 받아서 가공한다. */
const searchAndPush = (keyword) => {
    const API_KEY = 'o2LOve16lj0NenYN8kEemw0FaoG5wKzd'
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

    const GiphyAPICall = new XMLHttpRequest()
    GiphyAPICall.open('GET', URL)
    GiphyAPICall.send()

    // requests.get(url)
    GiphyAPICall.addEventListener('load', e => {
        const parsedData = JSON.parse(e.target.response)
        pushToDOM(parsedData)
    })


    /* 3. GIF 파일들을 index.html(DOM)에 밀어 넣어서 보여준다. */
    const pushToDOM = data => {
        resultArea.innerHTML = null;
        const dataSet = data.data

        dataSet.forEach(imgData => {
            let imgURL = imgData.images.original.url

            const elem = document.createElement('img')
            elem.src = imgURL
            elem.className = 'container-image'
            resultArea.appendChild(elem)
        })
    }
}

