import * as path from 'path'

const currentDir = __dirname; // Lấy đường dẫn tuyệt đối của thư mục

// console.log(currentDir)

const currentFile = __filename; // Lấy đường dẫn tuyệt đối của file hiện tại

// console.log(currentFile)

const examplePath = '/user/dev/documents/project/index.html'
const relativePath = 'assets/image/logo.png'
const windowPath = 'C:\\Users\\dev\\Documents\\file.txt'

const basename_default = path.basename(examplePath)

// console.log(basename_default)

const basename_file_ext = path.basename(examplePath, '.html')

// console.log(basename_file_ext)

// Trả về tên thư mục của đường dẫn

const dirnameExamplePath = path.dirname(examplePath)

// console.log(dirnameExamplePath)

const extName = path.extname(examplePath)

// console.log(extName)

const example1 = path.join(__dirname, 'data', 'example.txt')
const example2 = path.join(__dirname, '..', 'data', 'example.txt')

const example3 = path.join('/assets', 'image')


// console.log(example1)
// console.log(example2)
// console.log(example3)

/**
 * Path.resolve
 * Giải quyết một chuỗi hoặc chuỗi các đường dẫn thành một đường tuyệt đối
 * 
 */

// console.log(path.resolve('data', 'example.txt'))

console.log(path.isAbsolute(examplePath))
console.log(path.isAbsolute(relativePath))
console.log(path.isAbsolute(windowPath))