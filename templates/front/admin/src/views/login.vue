<template>
	<div>
		<div class="login-container">
			<el-form class="login_form animate__animated animate__backInLeft">
				<div class="login_form2">
					<div class="title-container">高校后勤报修系统设计与实现</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							账号：
						</div>
						<input placeholder="请输入账号：" name="username" type="text" v-model="rulesForm.username">
					</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							密码：
						</div>
						<div class="password-box">
							<input placeholder="请输入密码：" name="password" :type="showPassword?'text':'password'" v-model="rulesForm.password">
							<span class="icon iconfont" :class="showPassword?'icon-liulan13':'icon-liulan17'" @click="showPassword=!showPassword"></span>
						</div>
					</div>

					<div class="list-item select" v-if="roles.length>1">
						<div class="lable">
							角色：
						</div>
						<el-select v-model="rulesForm.role" placeholder="请选择角色：">
							<el-option v-if="loginType==1||(loginType==2&&item.roleName!='管理员')" v-for="item in roles" :key="item.roleName" :label="item.roleName" :value="item.roleName" />
						</el-select>
					</div>

		
					<div class="login-btn">
						<div class="login-btn1">
							<el-button v-if="loginType==1" type="primary" @click="login()" class="loginInBt">登录</el-button>
						</div>
						<div class="login-btn2">
							<el-button type="primary" @click="register('weixiurenyuan')" class="register">
								注册维修人员							</el-button>
							<el-button type="primary" @click="register('shenpiyuan')" class="register">
								注册审批员							</el-button>
						</div>
						<div class="login-btn3">
						</div>
					</div>
				</div>
			</el-form>
		</div>
	</div>
</template>
<script>
	import 'animate.css'
	import menu from "@/utils/menu";
	export default {
		data() {
			return {
				verifyCheck2: false,
				flag: false,
				baseUrl:this.$base.url,
				loginType: 1,
				rulesForm: {
					username: "",
					password: "",
					role: "",
				},
				menus: [],
				roles: [],
				tableName: "",
				showPassword: false,
			};
		},
		mounted() {
			let menus = menu.list();
			this.menus = menus;

			for (let i = 0; i < this.menus.length; i++) {
				if (this.menus[i].hasBackLogin=='是') {
					this.roles.push(this.menus[i])
				}
			}

		},
		created() {

		},
		destroyed() {
		},
		components: {
		},
		methods: {

			//注册
			register(tableName){
				this.$storage.set("loginTable", tableName);
				this.$router.push({path:'/register',query:{pageFlag:'register'}})
			},
			// 登陆
			login() {

				if (!this.rulesForm.username) {
					this.$message.error("请输入用户名");
					return;
				}
				if (!this.rulesForm.password) {
					this.$message.error("请输入密码");
					return;
				}
				if(this.roles.length>1) {
					if (!this.rulesForm.role) {
						this.$message.error("请选择角色");
						return;
					}

					let menus = this.menus;
					for (let i = 0; i < menus.length; i++) {
						if (menus[i].roleName == this.rulesForm.role) {
							this.tableName = menus[i].tableName;
						}
					}
				} else {
					this.tableName = this.roles[0].tableName;
					this.rulesForm.role = this.roles[0].roleName;
				}
		
				this.loginPost()
			},
			loginPost() {
				this.$http({
					url: `${this.tableName}/login?username=${this.rulesForm.username}&password=${this.rulesForm.password}`,
					method: "post"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.$storage.set("Token", data.token);
						this.$storage.set("role", this.rulesForm.role);
						this.$storage.set("sessionTable", this.tableName);
						this.$storage.set("adminName", this.rulesForm.username);
						this.$router.replace({ path: "/" });
					} else {
						this.$message.error(data.msg);
					}
				});
			},
		}
	}
</script>

<style lang="scss" scoped>
.login-container {
	min-height: 100vh;
	position: relative;
	background-repeat: no-repeat;
	background-position: center center;
	background-size: cover;
	background: url(http://codegen.caihongy.cn/20240903/f44ff97b83e04534a52ab964b81b825f.jpg);
	background-repeat: no-repeat;
	background-size: cover !important;
	background: url(http://codegen.caihongy.cn/20240903/f44ff97b83e04534a52ab964b81b825f.jpg);
	display: flex;
	width: 100%;
	min-height: 100vh;
	justify-content: center;
	align-items: center;
	background-position: center bottom;

	.login_form {
		padding: 40px 10% 20px 180px;
		margin: 0;
		z-index: 1000;
		display: flex;
		flex-wrap: wrap;
		border-radius: 50px;
		box-shadow: 0 1px 5px rgba(255,255,255,.5),inset 0px 0px 6px 0px rgba(74,103,82,1);
		flex-direction: column;
		background: linear-gradient(90deg, rgba(74,103,82,.05) 0%, rgba(74,103,82,.5) 25%,rgba(74,103,82,.8) 75%, rgba(74,103,82,.5) 100%);
		width: 45%;
		align-items: center;
		position: relative;
		height: auto;
		.login_form2 {
			width: 100%;
		}
		.title-container {
			padding: 0 0px;
			margin: 0 0 20px 0;
			color: #fff;
			background: none;
			font-weight: 600;
			width: 100%;
			font-size: 22px;
			line-height: 40px;
			text-align: center;
		}
		.list-item {
			padding: 0;
			margin: 0 0 26px;
			display: flex;
			width: calc(100% - 0px);
			align-items: center;
			position: relative;
			flex-wrap: wrap;
			.lable {
				color: #fff;
				left: -120px;
				width: 120px;
				font-size: 16px;
				line-height: 40px;
				position: absolute;
				text-align: right;
			}
			input {
				border: 0px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px;
				color: #ccc;
				background: rgba(0, 0, 0, .2);
				width: 100%;
				font-size: 16px;
				height: 40px;
			}
			input:focus {
				border: 0px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px;
				outline: none;
				color: #666;
				background: #fff;
				width: 100%;
				font-size: 16px;
				height: 40px;
			}
			.password-box {
				display: flex;
				width: 100%;
				position: relative;
				align-items: center;
				input {
					border: 0px solid #efeff7;
					border-radius: 20px;
					padding: 0 10px;
					color: #ccc;
					background: rgba(0, 0, 0, .2);
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				input:focus {
					border: 0px solid #efeff7;
					border-radius: 20px;
					padding: 0 10px;
					outline: none;
					color: #666;
					background: #fff;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.iconfont {
					cursor: pointer;
					z-index: 1;
					color: #ccc;
					top: 0;
					font-size: 16px;
					line-height: 44px;
					position: absolute;
					right: 12px;
				}
			}
			input::placeholder {
				color: #999;
				font-size: 16px;
			}
			/deep/ .el-select {
				width: 100%;
			}
			/deep/ .el-select .el-input__inner {
				border: 0px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px;
				color: #ccc;
				background: rgba(0, 0, 0, .2);
				width: 100%;
				font-size: 16px;
				height: 40px;
			}
			/deep/ .el-select .is-focus .el-input__inner {
				border: 1px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px;
				outline: none;
				color: #666;
				background: #fff;
				width: 100%;
				font-size: 16px;
				height: 40px;
			}
			/deep/ .el-select .el-input__inner::placeholder{
				color: #999;
				font-size: 16px;
			}
		}
		.login-btn {
			margin: 20px auto;
			display: flex;
			width: 100%;
			justify-content: center;
			align-items: center;
			flex-wrap: wrap;
			.login-btn1 {
				margin: 0 0 10px;
				width: 100%;
			}
			.login-btn2 {
				display: flex;
				width: 100%;
				justify-content: center;
				align-items: center;
				flex-wrap: wrap;
			}
			.login-btn3 {
				width: 100%;
			}
			.loginInBt {
				border: 0px solid rgba(0, 0, 0, 1);
				cursor: pointer;
				padding: 0 10px;
				margin: 0 0 10px;
				color: #fff;
				font-weight: 600;
				letter-spacing: 8px;
				font-size: 16px;
				border-radius: 30px;
				background: linear-gradient(90deg, rgba(74,103,82,1) 0%, rgba(94,168,164,1) 100%),#6a8b73;
				width: 100%;
				min-width: 68px;
				height: 44px;
			}
			.loginInBt:hover {
				opacity: 1;
			}
			.register {
				border: 0px solid rgba(0, 0, 0, 1);
				cursor: pointer;
				border-radius: 20px;
				padding: 0 10px;
				margin: 0 5px 10px;
				color: #4d5336;
				background: #cbccc2;
				width: auto;
				font-size: 16px;
				height: 36px;
			}
			.register:hover {
				opacity: 1;
			}
			.forget {
				border: 0;
				cursor: pointer;
				border-radius: 0;
				padding: 0;
				margin: 0 10px 10px 0;
				color: #fff;
				background: none;
				width: 100%;
				font-size: 15px;
				text-align: right;
				height: 34px;
			}
			.forget:hover {
				opacity: 1;
			}
		}
	}
}

</style>
