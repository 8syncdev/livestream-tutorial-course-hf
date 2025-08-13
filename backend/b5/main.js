// function greet(name, callback) {
//     console.log(name)
//     callback()
// }

// function sayGoodbye() {
//     console.log('Tạm biệt')
// }

// greet('Nam', sayGoodbye)

// console.log('Bắt đầu')

// setTimeout(() => {
//     console.log('Tác vụ bất đồng bộ hoàn thành trong 2 giây')
// }, 2000)

// console.log('Kết thúc')

// const fetchData = (url, callback) => {
//     setTimeout(() => {
//         const success = Math.random() > 0.5
//         // Giả định là nếu random > 0.5

//         if (success) {
//             const data = {
//                 message: 'Dữ liệu tải lên thành công ' + url
//             }
//             callback(null, data)
//         }
//         else {
//             const error = new Error('Không thể tải dữ liệu lên ' + url)
//             callback(error, null)
//         }
//     })
// }

// fetchData("https://api.example.com/data", (error, data) => {
//     if (error) {
//         console.log("Lỗi: ", error.message)
//     } else {
//         console.log("Dữ liệu nhận được là: " + data.message)
//     }
// })

// Callback Hell, Pyramid of Doom
// const getData = (callback1) => {
//     callback1(() => {
//         callback3(() => {
//             callback4()
//         })
//     })
// }


const fetchDataWithPromise = (url) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const success = Math.random() > 0.5
            if (success) {
                const data = {
                    message: 'Dữ liệu được tải thành công'
                }
                resolve(data)
            }
            else {
                const error = new Error('Không thể tải dữ liệu lên được')
                reject(error)
            }
        }, 1000)
    })
}

// fetchDataWithPromise("https://api.example.com/data-promise")
//     .then(data => {
//         console.log('Dữ liệu nhận được là: ' + data.message)
//     })
//     .catch(error => {
//         console.error('Lỗi Promise ', error.message)
//     })

const processData = async () => {
    try {
        console.log('Băt đầu xử lý dữ liệu...')
        const data1 = await fetchDataWithPromise("https://api.example.com/data-promise")

        console.log("Nhận dữ liệu data 1", data1.message)
    }
    catch (error) {
        console.log("Lỗi trong quá trình xử lý: ", error.message)
    }
    finally {
        console.log('Kết thức quá trình xử lý dữ liệu')
    }
}

processData()