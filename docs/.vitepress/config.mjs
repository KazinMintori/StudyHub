import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

const base = process.env.BASE_PATH || (process.env.GITHUB_ACTIONS ? '/Study_UET/' : '/')

export default withMermaid(
  defineConfig({
    base,
    title: 'UET Study Hub',
    description: 'Kho kiến thức ôn tập các môn học UET - Tối giản, trực quan, dễ hiểu',
    lang: 'vi-VN',
    head: [
      ['link', { rel: 'icon', href: '/favicon.ico' }],
      ['meta', { name: 'theme-color', content: '#3eaf7c' }]
    ],
    markdown: {
      math: true,
      lineNumbers: true
    },
    mermaid: {
      theme: 'default',
      themeVariables: {
        fontSize: '14px',
        fontFamily: 'Inter, system-ui, -apple-system, sans-serif'
      },
      flowchart: {
        htmlLabels: true,
        padding: 18,
        curve: 'basis'
      }
    },
    appearance: true,
    themeConfig: {
      darkModeSwitchLabel: 'Giao diện',
      lightModeSwitchTitle: 'Chuyển sang giao diện sáng',
      darkModeSwitchTitle: 'Chuyển sang giao diện tối',
      siteTitle: '📚 UET Study Hub',
      logo: '/logo.svg',
      nav: [
        { text: 'Trang chủ', link: '/' },
        {
          text: 'Học kỳ Hiện tại (5 Môn)',
          items: [
            { text: '🧠 Biểu diễn tri thức & Tìm kiếm nâng cao', link: '/bieu-dien-tri-thuc/' },
            { text: '🤖 Cơ sở toán cho AI', link: '/toan-cho-ai/' },
            { text: '🎲 Xác suất thống kê', link: '/xac-suat-thong-ke/' },
            { text: '🐍 Lập trình xử lý dữ liệu', link: '/xu-ly-du-lieu/' },
            { text: '⚡ Vật lý đại cương 2', link: '/vat-ly-2/' }
          ]
        },
        {
          text: 'Môn học khác',
          items: [
            { text: '📊 Giải thuật nền tảng cho KH Dữ liệu', link: '/giai-thuat-du-lieu/' },
            { text: '⚡ Cấu trúc dữ liệu & Giải thuật', link: '/dsa/' },
            { text: '📐 Toán rời rạc', link: '/discrete-math/' }
          ]
        },
        { text: 'Hướng dẫn học', link: '/guide/' }
      ],
      sidebar: {
        '/bieu-dien-tri-thuc/': [
          {
            text: 'Mục lục & Lộ trình',
            items: [
              { text: '0. Mục lục & Khung chương trình', link: '/bieu-dien-tri-thuc/' }
            ]
          },
          {
            text: 'Phần I: Tìm kiếm (Search)',
            items: [
              { text: 'Chương 2: Tìm kiếm mù (BFS, DFS, UCS, IDS)', link: '/bieu-dien-tri-thuc/02-tim-kiem-mu' },
              { text: 'Chương 3: Tìm kiếm kinh nghiệm (Greedy, A*)', link: '/bieu-dien-tri-thuc/03-tim-kiem-kinh-nghiem' },
              { text: 'Chương 4: Tìm kiếm có đối thủ (Minimax, Alpha–Beta)', link: '/bieu-dien-tri-thuc/04-tim-kiem-doi-khang' }
            ]
          },
          {
            text: 'Phần IV: Logic & Biểu diễn Tri thức',
            items: [
              { text: 'Chương 14: Logic & Biểu diễn tri thức (FOL)', link: '/bieu-dien-tri-thuc/14-logic-bieu-dien-tri-thuc' }
            ]
          }
        ],
        '/toan-cho-ai/': [
          {
            text: 'Cơ sở Toán cho AI',
            items: [
              { text: '0. Tổng quan & Lộ trình môn học', link: '/toan-cho-ai/' },
              { text: 'Bài 01: Nhập môn Giới thiệu về Tối ưu', link: '/toan-cho-ai/bai-01-nhap-mon-toi-uu' },
              { text: 'Bài 02: Tập lồi: Hình học của những lựa chọn', link: '/toan-cho-ai/bai-02-tap-loi' }
            ]
          }
        ],
        '/xac-suat-thong-ke/': [
          {
            text: 'Xác suất Thống kê',
            items: [
              { text: '1. Tổng quan & Lộ trình môn học', link: '/xac-suat-thong-ke/' }
            ]
          }
        ],
        '/xu-ly-du-lieu/': [
          {
            text: 'Lập trình Xử lý Dữ liệu',
            items: [
              { text: '0. Tổng quan & Lộ trình môn học', link: '/xu-ly-du-lieu/' },
              { text: 'Bài 1: Tổng quan, Công cụ & Chính sách AI', link: '/xu-ly-du-lieu/bai-01-tong-quan-cong-cu-chinh-sach-ai' },
              { text: 'Bài 2: Python cơ bản cho xử lý dữ liệu', link: '/xu-ly-du-lieu/bai-02-python-co-ban' },
              { text: 'Bài 3: NumPy và tư duy vector hoá', link: '/xu-ly-du-lieu/bai-03-numpy' },
              { text: 'Bài 4: Làm quen với pandas', link: '/xu-ly-du-lieu/bai-04-lam-quen-pandas' },
              { text: 'Bài 5: Series & DataFrame chuyên sâu', link: '/xu-ly-du-lieu/bai-05-series-dataframe-chuyen-sau' }
            ]
          }
        ],
        '/vat-ly-2/': [
          {
            text: 'Vật lý Đại cương 2',
            items: [
              { text: '1. Tổng quan & Lộ trình môn học', link: '/vat-ly-2/' }
            ]
          }
        ],
        '/giai-thuat-du-lieu/': [
          {
            text: 'Giải thuật nền tảng cho KH Dữ liệu',
            items: [
              { text: '0. Mục lục & Lộ trình môn học', link: '/giai-thuat-du-lieu/' }
            ]
          }
        ],
        '/dsa/': [
          {
            text: 'Cấu trúc dữ liệu & Giải thuật',
            items: [
              { text: '1. Giới thiệu & Lộ trình học', link: '/dsa/' },
              { text: '2. Phân tích độ phức tạp thuật toán', link: '/dsa/complexity' },
              { text: '3. Thuật toán Sắp xếp (Sorting)', link: '/dsa/sorting' },
              { text: '4. Thuật toán Tìm kiếm (Searching)', link: '/dsa/searching' },
              { text: '5. Cấu trúc Cây & Cây nhị phân', link: '/dsa/trees' },
              { text: '6. Đồ thị & Các thuật toán duyệt', link: '/dsa/graphs' }
            ]
          }
        ],
        '/discrete-math/': [
          {
            text: 'Toán rời rạc',
            items: [
              { text: '1. Tổng quan & Lộ trình', link: '/discrete-math/' },
              { text: '2. Logic mệnh đề & Vị từ', link: '/discrete-math/logic' },
              { text: '3. Quan hệ & Ánh xạ', link: '/discrete-math/relations' },
              { text: '4. Lý thuyết Đồ thị cơ bản', link: '/discrete-math/graph-theory' }
            ]
          }
        ],
        '/guide/': [
          {
            text: 'Hướng dẫn sử dụng Hub',
            items: [
              { text: 'Phương pháp học hiệu quả', link: '/guide/' },
              { text: 'Cách đóng góp & Thêm môn học', link: '/guide/contribute' }
            ]
          }
        ]
      },
      search: {
        provider: 'local',
        options: {
          locales: {
            root: {
              translations: {
                button: {
                  buttonText: 'Tìm kiếm bài học...',
                  buttonAriaLabel: 'Tìm kiếm tài liệu'
                },
                modal: {
                  noResultsText: 'Không tìm thấy kết quả cho',
                  resetButtonTitle: 'Xóa tìm kiếm',
                  footer: {
                    selectText: 'để chọn',
                    navigateText: 'để điều hướng',
                    closeText: 'để đóng'
                  }
                }
              }
            }
          }
        }
      },
      outline: {
        level: [2, 3],
        label: 'Mục lục bài viết'
      },
      docFooter: {
        prev: 'Bài trước',
        next: 'Bài tiếp theo'
      },
      lastUpdated: {
        text: 'Cập nhật lần cuối'
      },
      footer: {
        message: 'Xây dựng với tâm huyết dành cho sinh viên UET 🎓',
        copyright: 'Bản quyền nội dung © 2026 UET Study Hub'
      }
    }
  })
)
