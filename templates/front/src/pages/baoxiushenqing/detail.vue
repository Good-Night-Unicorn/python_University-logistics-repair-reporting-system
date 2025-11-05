<template>
	<div>
	<!--  -->
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'·'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index" :to="'/index/baoxiushenqing?centerType=' + (centerType?'1':'0')"><a>{{item.name}}</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item3"><a href="javascript:void(0);">详情</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="detail-preview">
			<div class="attr">
				<div class="info">
					<div class="title-item">
						<div class="detail-title">
							{{detail.baoxiumingcheng}}
						</div>
					</div>
					<div class="item">
						<div class="lable">报修单号</div>
						<div class="text "  >{{detail.baoxiudanhao}}</div>
					</div>
					<div class="item">
						<div class="lable">报修类型</div>
						<div class="text "  >{{detail.baoxiuleixing}}</div>
					</div>
					<div class="item">
						<div class="lable">报修地点</div>
						<div class="text "  >{{detail.baoxiudidian}}</div>
					</div>
					<div class="item">
						<div class="lable">紧急程度</div>
						<div class="text "  >{{detail.jinjichengdu}}</div>
					</div>
					<div class="item">
						<div class="lable">申请时间</div>
						<div class="text "  >{{detail.shenqingshijian}}</div>
					</div>
					<div class="item">
						<div class="lable">故障描述</div>
						<div class="text "  >{{detail.guzhangmiaoshu}}</div>
					</div>
					<div class="item">
						<div class="lable">账号</div>
						<div class="text "  >{{detail.zhanghao}}</div>
					</div>
					<div class="item">
						<div class="lable">姓名</div>
						<div class="text "  >{{detail.xingming}}</div>
					</div>
					<div class="item">
						<div class="lable">手机</div>
						<div class="text "  >{{detail.shouji}}</div>
					</div>
					<div class="item">
						<div class="lable">审批状态</div>
						<div class="text "  >{{detail.shenpizhuangtai}}</div>
					</div>
					<div class="item" v-if="centerType">
						<div class="lable">审核状态</div>
						<div class="text">{{detail.sfsh=='是'?'通过':(detail.sfsh=='否'?'不通过':'待审核')}}</div>
					</div>
					<div class="item" v-if="centerType">
						<div class="lable">审核回复</div>
						<div class="text">{{detail.shhf}}</div>
					</div>
					<div class="btn_box">
						<el-button class="editBtn" v-if="btnAuth('baoxiushenqing','修改')&&detail.sfsh!='是'&&detail.sfsh!='否' " @click="editClick">修改</el-button>
						<el-button class="delBtn" v-if="btnAuth('baoxiushenqing','删除')" @click="delClick">删除</el-button>
						<el-button class="reserveBtn" 
							v-if="btnAuth('baoxiushenqing','审批')" 
							@click="onAcross('baoxiushenpi','是','','shenpizhuangtai','已审批','已审批,未审批'.split(',')[0])" type="warning">
							审批
						</el-button>
						<el-button class="auditBtn" v-if="btnAuth('baoxiushenqing','审核') && (detail.sfsh=='待审核'||!detail.sfsh)" @click="onSH" type="warning">审核</el-button>
					</div>
				</div>
			</div>
		
			<div class="swiper3" v-if="detailBanner.length">
				<div class="big">
					<img id="big" :src="swiperBigUrl" class="image">
				</div>
				<div class="samll">
					<div class="swiper3-small-item" v-for="item in detailBanner" :key="item.id">
						<img v-if="item.substr(0,4)=='http'" :src="item" @click="swiperClick3(item)" class="image">
						<img v-else :src="baseUrl + item" @click="swiperClick3(baseUrl + item)" class="image">
					</div>
				</div>
			</div>


		

			<el-tabs class="detail-tabs" v-model="activeName" type="border-card" v-if="tabsNum>0" >
			</el-tabs>
			<el-dialog title="审核" :visible.sync="sfshVisiable" width="50%">
				<el-form ref="shForm" :model="shForm" label-width="80px">
					<el-form-item label="审核状态">
						<el-select v-model="shForm.sfsh" placeholder="审核状态">
							<el-option label="通过" value="是"></el-option>
							<el-option label="不通过" value="否"></el-option>
							<el-option label="待审核" value="待审核"></el-option>
						</el-select>
					</el-form-item>
					<el-form-item label="内容">
						<el-input type="textarea" :rows="8" v-model="shForm.shhf"></el-input>
					</el-form-item>
				</el-form>
				<div slot="footer" class="dialog-footer">
					<el-button @click="sfshVisiable = false">取 消</el-button>
					<el-button type="primary" @click="shHandler">确 定</el-button>
				</div>
			</el-dialog>

		</div>
		<div class="share_view">
		</div>
	</div>
</template>

<script>
	import axios from 'axios'
	import Swiper from "swiper";
	export default {
		//数据集合
		data() {
			return {
				tablename: 'baoxiushenqing',
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '报修申请'
					}
				],
				title: '',
				detailBanner: [],
				userid: localStorage.getItem('frontUserid'),
				id: 0,
				detail: {},
				tabsNum: 0,
				activeName: 'first',
				total: 1,
				pageSize: 10,
				totalPage: 1,
				buynumber: 1,
				sfshVisiable: false,
				shForm: {
					sfsh: '是',
					shhf: ''
				},
				centerType: false,
				storeupType: false,
				shareUrl: location.href,
				swiperBigUrl: null,
			}
		},
		created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0) {
				this.centerType = true
			}
			if(this.$route.query.storeupType&&this.$route.query.storeupType!=0) {
				this.storeupType = true
			}
			
			this.init();
		},
		mounted() {
		},
		//方法集合
		methods: {
			swiperClick3(src) {
				this.swiperBigUrl = src
			},
			init() {
				this.id = this.$route.query.id
				this.baseUrl = this.$config.baseUrl;
				this.$http.get(this.tablename + '/detail/'  + this.id, {}).then(res => {
					if (res.data.code == 0) {
						this.detail = res.data.data;
						this.title = this.detail.baoxiumingcheng;
						if(this.detail.fengmian) {
							this.detailBanner = this.detail.fengmian.split(",w").length>1?[this.detail.fengmian]:this.detail.fengmian.split(',');
						}
						this.$forceUpdate();
						if(localStorage.getItem('frontToken')){
						}

					}
					if (this.detailBanner.length) {
						if (this.detailBanner[0].substr(0,4)=='http') {
							this.swiperBigUrl = this.detailBanner[0]
						} else {
							this.swiperBigUrl = this.baseUrl + this.detailBanner[0]
						}
					}
				});
			},
			async onAcross(acrossTable,crossOptAudit,crossOptPay,statusColumnName,tips,statusColumnValue,type=1){
				if(crossOptAudit=='是'&&this.detail.sfsh!='是') {
					this.$message({
						message: "请审核通过后再操作",
						type: "error",
						duration: 1500,
						onClose: () => {
						}
					});
					return
				}
				localStorage.setItem('crossTable',`baoxiushenqing`);
				localStorage.setItem('crossObj', JSON.stringify(this.detail));
				localStorage.setItem('statusColumnName',statusColumnName);
				localStorage.setItem('statusColumnValue',statusColumnValue);
				localStorage.setItem('tips',tips);
				if(statusColumnName!=''&&!statusColumnName.startsWith("[")) {
					var obj = JSON.parse(localStorage.getItem('crossObj'));
					for (var o in obj){
						if(o==statusColumnName && obj[o]==statusColumnValue){
							this.$message({
								type: 'error',
								message: tips,
								duration: 1500
							});
							return
						}
					}
				}
				this.$router.push({path: '/index/' + acrossTable + 'Add', query: {type: 'cross'}});
			},
			onSH() {
				this.sfshVisiable = true;
			},
			shHandler(){
				this.$confirm(`确定操作?`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(() => {
					this.detail.sfsh = this.shForm.sfsh;
					this.detail.shhf = this.shForm.shhf;
					this.$http.post(`${this.tablename}/update`, this.detail).then(res => {
						if (res.data.code == 0) {
							this.sfshVisiable = false;
							this.$message({
								message: "操作成功",
								type: "success",
								duration: 1500,
							});
						}
					});
				});
			},
			curChange(page) {
				this.getDiscussList(page);
			},
			prevClick(page) {
				this.getDiscussList(page);
			},
			nextClick(page) {
				this.getDiscussList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getDiscussList(1);
			},
			// 返回按钮
			backClick(){
				if(this.storeupType){
					history.back()
				}else{
					let params = {}
					if(this.centerType){
						params.centerType = 1
					}
					this.$router.push({path: '/index/baoxiushenqing', query: params});
				}
			},
			// 下载
			download(file ){
				if(!file) {
					this.$message({
						type: 'error',
						message: '文件不存在',
						duration: 1500,
					});
					return;
				}
				let arr = file.replace(new RegExp('upload/', "g"), "")
				axios.get(this.baseUrl + '/file/download?fileName=' + arr, {
					headers: {
						token: localStorage.getItem("frontToken")
					},
					responseType: "blob"
				}).then(({
					data
				}) => {
					const binaryData = [];
					binaryData.push(data);
					const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
						type: 'application/pdf;chartset=UTF-8'
					}))
					const a = document.createElement('a')
					a.href = objectUrl
					a.download = arr
					// a.click()
					// 下面这个写法兼容火狐
					a.dispatchEvent(new MouseEvent('click', {
						bubbles: true,
						cancelable: true,
						view: window
					}))
					window.URL.revokeObjectURL(data)
				},err=>{
					axios.get((location.href.split(this.$config.name).length>1 ? location.href.split(this.$config.name)[0] :'') + this.$config.name + '/file/download?fileName=' + arr, {
						headers: {
							token: localStorage.getItem("frontToken")
						},
						responseType: "blob"
					}).then(({
						data
					}) => {
						const binaryData = [];
						binaryData.push(data);
						const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
							type: 'application/pdf;chartset=UTF-8'
						}))
						const a = document.createElement('a')
						a.href = objectUrl
						a.download = arr
						// a.click()
						// 下面这个写法兼容火狐
						a.dispatchEvent(new MouseEvent('click', {
							bubbles: true,
							cancelable: true,
							view: window
						}))
						window.URL.revokeObjectURL(data)
					})
				})
			},


			// 权限判断
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			// 修改
			editClick(){
				this.$router.push(`/index/baoxiushenqingAdd?type=edit&&id=${this.detail.id}`);
			},
			// 删除
			async delClick(){
				await this.$confirm('是否删除此报修申请？') .then(_ => {
					this.$http.post('baoxiushenqing/delete', [this.detail.id]).then(async res => {
						if (res.data.code == 0) {
							this.$message({
								type: 'success',
								message: '删除成功!',
								duration: 1500,
								onClose: () => {
									history.back()
								}
							});
						}
					});
				}).catch(_ => {});
			},
		},
		components: {
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.detail-preview {
		padding: 50px 16%;
		margin: 10px auto;
		background: url(http://codegen.caihongy.cn/20250109/9f2a54e864404d27835768df2d9ef3bb.png) top left/100% 1100px no-repeat;
		display: flex;
		width: 100%;
		align-items: flex-start;
		position: relative;
		flex-wrap: wrap;
		.attr {
			padding: 20px;
			margin: 0 0 120px;
			background: none;
			flex: 1;
			display: flex;
			width: 65%;
			min-height: 1000px;
			position: relative;
			order: 2;
			.info {
				padding: 0;
				margin: 0 0 0 10px;
				background: #fff;
				flex: 1;
				.title-item {
					border: 1px solid #7D9E38;
					padding: 5px 10px;
					margin: 0 0 10px 0;
					background: none;
					display: flex;
					border-width: 0 1px 1px;
					justify-content: space-between;
					align-items: center;
					.detail-title {
						color: #7D9E38;
						font-weight: bold;
						font-size: 16px;
					}
				}
				.item {
					padding: 13px 5px;
					box-shadow: 0 4px 8px rgba(125, 158, 56,.3);
					margin: 0 0 5px;
					background: none;
					display: flex;
					justify-content: spaceBetween;
					align-items: center;
					.lable {
						padding: 0 10px;
						color: #7D9E38;
						white-space: nowrap;
						width: auto;
						font-size: 14px;
						line-height: 24px;
						text-align: right;
						height: auto;
					}
					.text {
						padding: 0 10px;
						color: #7D9E38;
						word-break: break-all;
						flex: 1;
						font-size: 14px;
						line-height: 24px;
						height: auto;
					}
					.price {
						color: #f00;
					}
					.bold {
						font-weight: bold;
					}
					.link {
						cursor: pointer;
						text-decoration: underline;
					}
				}
				.btn_box {
					padding: 10px 0;
					display: flex;
					flex-wrap: wrap;
				}
				.editBtn {
					border: 0;
					cursor: pointer;
					border-radius: 0;
					padding: 0 10px;
					margin: 0 5px 0 0;
					outline: none;
					color: #fff;
					background: #61A677;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.editBtn:hover {
					opacity: 0.7;
				}
				.delBtn {
					border: 0;
					cursor: pointer;
					border-radius: 0;
					padding: 0 10px;
					margin: 0 5px 0 0;
					outline: none;
					color: #fff;
					background: #859A5E;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.delBtn:hover {
					opacity: 0.7;
				}
				.auditBtn {
					border: 0;
					cursor: pointer;
					border-radius: 0;
					padding: 0 10px;
					margin: 0 5px 0 0;
					outline: none;
					color: #fff;
					background: #81AF79;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.auditBtn:hover {
					opacity: 0.7;
				}
			}
		}
		.swiper3 {
			padding: 20px 0 0;
			background: #fff;
			width: 35%;
			height: auto;
			order: 1;
			.big {
				margin: 0 0 20px;
				background: #fff;
				width: 100%;
				height: 660px;
				img {
					object-fit: cover;
					display: block;
					width: 100%;
					height: 100%;
				}
			}
			.samll {
				padding: 0 5px;
				background: #fff;
				display: flex;
				width: 100%;
				height: 100px;
				.swiper3-small-item {
					margin: 0 2px;
					flex: 1;
					height: 100%;
					img {
						object-fit: cover;
						display: block;
						width: 100%;
						height: 100%;
					}
				}
			}
		}
		.detail-tabs {
			border: 0px solid #DCDFE6;
			border-radius: 10px;
			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, .1);
			background: #FFF;
			width: 100%;
			order: 5;
			& /deep/ .el-tabs__header .el-tabs__nav-wrap {
				margin-bottom: 0;
			}
			/deep/ .el-tabs__header {
				border-radius: 10px 10px 0 0;
				padding: 10px 20px;
				margin: 0;
				background: #7D9E38;
				border-color: #E4E7ED;
				border-width: 0;
				border-style: solid;
			}
			
			/deep/ .el-tabs__header .el-tabs__item {
				border: 0;
				padding: 0 20px;
				margin: 0 10px;
				color: #fff;
				background: transparent;
				font-weight: 500;
				display: inline-block;
				font-size: 14px;
				line-height: 30px;
				position: relative;
				list-style: none;
				height: 30px;
			}
			
			/deep/ .el-tabs__header .el-tabs__item:hover {
				border: 0;
				color: #7D9E38;
				background: #FFF;
			}
			
			/deep/ .el-tabs__header .el-tabs__item.is-active {
				border: 0;
				color: #7D9E38;
				background: #FFF;
			}
			
			/deep/ .el-tabs__content {
				padding: 15px;
			}
		}
	}
	.share_view{
		box-shadow: 0 1px 6px rgba(0,0,0,.3);
		z-index: 11;
		bottom: 20%;
		background: #fff;
		position: fixed;
		right: 0;
		.share:last-of-type{
			border:none;
		}
	}
</style>
