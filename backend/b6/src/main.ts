import * as http from 'http'
import * as url from 'url'


const PORT = 8000

const server = http.createServer((req: http.IncomingMessage, res: http.ServerResponse) => {
    // 1. Phân tích url
    // url.parse(): phân tích url
    const parseUrl = url.parse(req.url || '/', true)
    const path = parseUrl.pathname
    const query = parseUrl.query
    const method = req.method

    console.log(`
        đường dẫn: ${path}
        phương thức: ${method}
        Query params: ${JSON.stringify(query)}
        `)

    res.setHeader(
        'Content-Type', 'text/plain; charset=utf-8'
    )

    res.end(
        "Hello Server"
    )
})

server.listen(PORT, () => {
    console.log(`127.0.0.1:${PORT}`)
})