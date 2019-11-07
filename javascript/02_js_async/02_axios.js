// const DogAPI = new XMLHttpRequest 

// DogAPI.open()
// DogAPI.send()
// DogAPI.addEventListener

const URL = "https://dog.ceo/api/breeds/image/random"
const URL2 = "https://api.thecatapi.com/v1/images/search"

const dogButton = document.querySelector('#dog')
const catButton = document.querySelector('#cat')

const getDogAndPush = () => {
    axios.get(URL)
        .then(response => {
            // 바디 아래에 이미지 태그 넣어준다.
            const imgURL = response.data.message
            const imgTag = document.createElement('img')
            imgTag.src = imgURL
            document.querySelector('#show').appendChild(imgTag)
        })
}

const getCatandPush = () => {
    axios.get(URL2)
        .then(response => {
            const imgURL = response.data[0].url
            const imgTag = document.createElement('img')
            imgTag.src = imgURL
            document.querySelector('#show').appendChild(imgTag)
        }) 
}

dogButton.addEventListener('click', getDogAndPush)
catButton.addEventListener('click', getCatandPush)

// 콜백부분
// 1. axios -> dog 사진 요청
// 2. <body> 아래에 <img> 받아온 사진 보여주기



// const result = axios.get(URL)
// // Promise 객체 (resolved)

// // promise 객체를 까보기 위해서  .then()
// result.then((result) => {
//     // console.log(result.data.message)
// })

// axios.get(URL)
//     .then(result => console.log(result.data.message))
