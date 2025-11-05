const base = {
    get() {
        return {
            url : "http://localhost:8080/django79tvn57g/",
            name: "django79tvn57g",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "高校后勤报修系统设计与实现"
        } 
    }
}
export default base
