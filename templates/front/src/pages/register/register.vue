<template>
	<div>

		<div class="container">
			<el-form class='rgs-form animate__animated animate__bounce' v-if="pageFlag=='register'" ref="registerForm" :model="registerForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">高校后勤报修系统设计与实现注册</p></div>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="zhanghao">
						<div class="label" :class="changeRules('zhanghao')?'required':''">账号：</div>
						<el-input v-model="registerForm.zhanghao"  placeholder="请输入账号" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="xingming">
						<div class="label" :class="changeRules('xingming')?'required':''">姓名：</div>
						<el-input v-model="registerForm.xingming"  placeholder="请输入姓名" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="mima">
						<div class="label" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="mima2">
						<div class="label" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="xingbie">
						<div class="label" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in yonghuxingbieOptions"
								:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="shouji">
						<div class="label" :class="changeRules('shouji')?'required':''">手机：</div>
						<el-input v-model="registerForm.shouji"  placeholder="请输入手机" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="touxiang">
						<div class="label" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="1"
							:multiple="true"
							:fileUrls="registerForm.touxiang?registerForm.touxiang:''"
							@change="yonghutouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'" prop="weixiuzhanghao">
						<div class="label" :class="changeRules('weixiuzhanghao')?'required':''">维修账号：</div>
						<el-input v-model="registerForm.weixiuzhanghao"  placeholder="请输入维修账号" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'" prop="mima">
						<div class="label" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'" prop="mima2">
						<div class="label" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'" prop="weixiuxingming">
						<div class="label" :class="changeRules('weixiuxingming')?'required':''">维修姓名：</div>
						<el-input v-model="registerForm.weixiuxingming"  placeholder="请输入维修姓名" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'" prop="xingbie">
						<div class="label" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in weixiurenyuanxingbieOptions"
								:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'" prop="lianxifangshi">
						<div class="label" :class="changeRules('lianxifangshi')?'required':''">联系方式：</div>
						<el-input v-model="registerForm.lianxifangshi"  placeholder="请输入联系方式" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'" prop="touxiang">
						<div class="label" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="1"
							:multiple="true"
							:fileUrls="registerForm.touxiang?registerForm.touxiang:''"
							@change="weixiurenyuantouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'" prop="shenpizhanghao">
						<div class="label" :class="changeRules('shenpizhanghao')?'required':''">审批账号：</div>
						<el-input v-model="registerForm.shenpizhanghao"  placeholder="请输入审批账号" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'" prop="mima">
						<div class="label" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'" prop="mima2">
						<div class="label" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'" prop="shenpixingming">
						<div class="label" :class="changeRules('shenpixingming')?'required':''">审批姓名：</div>
						<el-input v-model="registerForm.shenpixingming"  placeholder="请输入审批姓名" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'" prop="xingbie">
						<div class="label" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in shenpiyuanxingbieOptions"
								:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'" prop="lianxishouji">
						<div class="label" :class="changeRules('lianxishouji')?'required':''">联系手机：</div>
						<el-input v-model="registerForm.lianxishouji"  placeholder="请输入联系手机" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'" prop="touxiang">
						<div class="label" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="1"
							:multiple="true"
							:fileUrls="registerForm.touxiang?registerForm.touxiang:''"
							@change="shenpiyuantouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<el-button class="register_btn" type="primary" @click="submitForm('registerForm')">注册</el-button>
						</div>
						<div class="register-btn2">
							<router-link class="has_btn" to="/login">已有账号，直接登录</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
		</div>
	</div>
</div>
</template>

<script>
	import 'animate.css';

export default {
    //数据集合
    data() {
		return {
            pageFlag : '',
			tableName: '',
			registerForm: {},
			forgetForm: {},
			rules: {},
			requiredRules: {},
            yonghuxingbieOptions: [],
            weixiurenyuanxingbieOptions: [],
            shenpiyuanxingbieOptions: [],
		}
    },
	mounted() {
		if(this.$route.query.pageFlag=='register'){
			this.tableName = this.$route.query.role;
			if(this.tableName=='yonghu'){
				this.registerForm = {
					zhanghao: '',
					xingming: '',
					mima: '',
					mima2: '',
					xingbie: '',
					shouji: '',
					touxiang: '',
				}
			}
			if(this.tableName=='weixiurenyuan'){
				this.registerForm = {
					weixiuzhanghao: '',
					mima: '',
					mima2: '',
					weixiuxingming: '',
					xingbie: '',
					lianxifangshi: '',
					touxiang: '',
				}
			}
			if(this.tableName=='shenpiyuan'){
				this.registerForm = {
					shenpizhanghao: '',
					mima: '',
					mima2: '',
					shenpixingming: '',
					xingbie: '',
					lianxishouji: '',
					touxiang: '',
				}
			}
			if ('yonghu' == this.tableName) {
				this.rules.zhanghao = [{ required: true, message: '请输入账号', trigger: 'blur' }];
				this.requiredRules.zhanghao = [{ required: true, message: '请输入账号', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.xingming = [{ required: true, message: '请输入姓名', trigger: 'blur' }];
				this.requiredRules.xingming = [{ required: true, message: '请输入姓名', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
				this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			this.yonghuxingbieOptions = "男,女".split(',');
			if ('yonghu' == this.tableName) {
				this.rules.shouji = [{ required: true, validator: this.$validate.isMobile, trigger: 'blur' }];
			}
			if ('weixiurenyuan' == this.tableName) {
				this.rules.weixiuzhanghao = [{ required: true, message: '请输入维修账号', trigger: 'blur' }];
				this.requiredRules.weixiuzhanghao = [{ required: true, message: '请输入维修账号', trigger: 'blur' }]
			}
			if ('weixiurenyuan' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
				this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('weixiurenyuan' == this.tableName) {
				this.rules.weixiuxingming = [{ required: true, message: '请输入维修姓名', trigger: 'blur' }];
				this.requiredRules.weixiuxingming = [{ required: true, message: '请输入维修姓名', trigger: 'blur' }]
			}
			this.weixiurenyuanxingbieOptions = "男,女".split(',');
			if ('weixiurenyuan' == this.tableName) {
				this.rules.lianxifangshi = [{ required: true, validator: this.$validate.isMobile, trigger: 'blur' }];
			}
			if ('shenpiyuan' == this.tableName) {
				this.rules.shenpizhanghao = [{ required: true, message: '请输入审批账号', trigger: 'blur' }];
				this.requiredRules.shenpizhanghao = [{ required: true, message: '请输入审批账号', trigger: 'blur' }]
			}
			if ('shenpiyuan' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
				this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('shenpiyuan' == this.tableName) {
				this.rules.shenpixingming = [{ required: true, message: '请输入审批姓名', trigger: 'blur' }];
				this.requiredRules.shenpixingming = [{ required: true, message: '请输入审批姓名', trigger: 'blur' }]
			}
			this.shenpiyuanxingbieOptions = "男,女".split(',');
			if ('shenpiyuan' == this.tableName) {
				this.rules.lianxishouji = [{ required: true, validator: this.$validate.isMobileNotNull, trigger: 'blur' }];
				this.requiredRules.lianxishouji = [{ required: true, message: '请输入联系手机', trigger: 'blur' }]
			}
		}
	},
    created() {
		this.pageFlag = this.$route.query.pageFlag;
    },
    //方法集合
    methods: {
		changeRules(name){
			if(this.requiredRules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
        // 下二随
		yonghutouxiangUploadChange(fileUrls) {
			this.registerForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
		},
		weixiurenyuantouxiangUploadChange(fileUrls) {
			this.registerForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
		},
		shenpiyuantouxiangUploadChange(fileUrls) {
			this.registerForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
		},

		// 多级联动参数


		submitForm(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					var url=this.tableName+"/register";
					if(`yonghu` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
						this.$message.error(`两次密码输入不一致`);
						return
					}
					if(`weixiurenyuan` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
						this.$message.error(`两次密码输入不一致`);
						return
					}
					if(`shenpiyuan` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
						this.$message.error(`两次密码输入不一致`);
						return
					}
					this.$http.post(url, this.registerForm).then(res => {
						if (res.data.code === 0) {
							this.$message({
								message: '注册成功',
								type: 'success',
								duration: 1500,
								onClose: () => {
									this.$router.push('/login');
								}
							});
						} else {
							this.$message.error(res.data.msg);
						}
					});
				} else {
					return false;
				}
			});
		},
		resetForm(formName) {
			this.$refs[formName].resetFields();
		}
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.container {
		background: url(http://codegen.caihongy.cn/20250109/ed3305ba73b5428e876ff4931832ef79.png) center center/100% 100%;
		display: flex;
		width: 100%;
		min-height: 100vh;
		justify-content: flex-start;
		align-items: center;
		position: relative;
		background: url(http://codegen.caihongy.cn/20250109/ed3305ba73b5428e876ff4931832ef79.png) center center/100% 100%;
		.rgs-form {
			border-radius: 10px;
			padding: 40px 20px 20px;
			box-shadow: 0px 5px 10px 0px rgba(0, 0, 0, 0.25);
			margin: 0 0 0 10%;
			z-index: 1;
			overflow: auto;
			background: #fff;
			width: 30%;
			height: 70vh;
			.rgs-form2 {
				flex-direction: column;
				display: flex;
				width: 100%;
				justify-content: space-between;
				height: 100%;
				.title {
					margin: 0 0 10px 0;
					color: #000;
					font-weight: bold;
					width: 100%;
					font-size: 26px;
					line-height: 44px;
					text-align: center;
				}
				.subtitle {
					margin: 0 0 10px 0;
					text-shadow: 4px 4px 2px rgba(64, 158, 255, .5);
					color: rgba(64, 158, 255, 1);
					width: 100%;
					font-size: 20px;
					line-height: 44px;
					text-align: center;
				}
				.list-item {
					box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
					padding: 0 0 0 10px;
					margin: 0 auto 10px;
					display: flex;
					width: 80%;
					align-items: center;
					order: 2;
					/deep/.el-form-item__content {
						display: flex;
						width: 100%;
						align-items: flex-start;
						.label {
							color: #7D9E38;
							width: 80px;
							font-size: 14px;
							line-height: 50px;
							height: 50px;
						}
						
						.required {
							position: relative;
						}
						.required::after{
							color: red;
							left: -10px;
							position: absolute;
							content: "*";
						}
						.el-input {
							width: calc(100% - 80px);
						}
						.el-input .el-input__inner {
							border: 0;
							border-radius: 8px;
							padding: 0 10px;
							box-shadow: 0 0 0px rgba(64, 158, 255, .5);
							outline: none;
							color: #666;
							width: 100%;
							font-size: 14px;
							height: 50px;
						}
						.el-input .el-input__inner:focus {
							border: 0;
							border-radius: 8px;
							padding: 0 10px;
							box-shadow: 0 0 0px rgba(64, 158, 255, .5);
							outline: none;
							color: #7D9E38;
							width: 100%;
							font-size: 14px;
							height: 50px;
						}
						.el-input-number {
							width: calc(100% - 80px);
						}
						.el-input-number .el-input__inner {
							text-align: left;
							border: 0;
							border-radius: 8px;
							padding: 0 10px;
							box-shadow: 0 0 0px rgba(64, 158, 255, .5);
							outline: none;
							color: #666;
							width: 100%;
							font-size: 14px;
							height: 50px;
						}
						.el-input-number .el-input-number__decrease {
							display: none;
						}
						.el-input-number .el-input-number__increase {
							display: none;
						}
						.el-select {
							width: calc(100% - 80px);
						}
						.el-select .el-input__inner {
							border: 0;
							border-radius: 0px;
							padding: 0 10px;
							box-shadow: 0 0 0px rgba(64, 158, 255, .5);
							outline: none;
							color: #666;
							width: 100%;
							font-size: 14px;
							height: 50px;
						}
						.el-select .el-input__inner:focus {
							border: 0;
							border-radius: 0px;
							padding: 0 10px;
							box-shadow: 0 0 0px rgba(64, 158, 255, .5);
							outline: none;
							color: #7D9E38;
							width: 100%;
							font-size: 14px;
							height: 50px;
						}
						.el-date-editor {
							width: calc(100% - 80px);
						}
						.el-date-editor .el-input__inner {
							border: 0;
							border-radius: 8px;
							padding: 0 10px 0 30px;
							box-shadow: 0 0 0px rgba(64, 158, 255, .5);
							outline: none;
							color: #666;
							width: 100%;
							font-size: 14px;
							height: 50px;
						}
						.el-date-editor .el-input__inner:focus {
							border: 0px solid rgba(85, 170, 0, 1.0);
							padding: 0 10px 0 30px;
							color: #7D9E38;
							width: 100%;
							font-size: 14px;
							height: 50px;
						}
						.el-upload--picture-card {
							background: transparent;
							border: 0;
							border-radius: 0;
							width: auto;
							height: auto;
							line-height: initial;
							vertical-align: middle;
						}
						.upload .upload-img {
							border: 1px dashed #7D9E38;
							cursor: pointer;
							border-radius: 8px;
							color: #7D9E38;
							width: 90px;
							font-size: 32px;
							line-height: 90px;
							text-align: center;
							height: 90px;
						}
						.el-upload-list .el-upload-list__item {
							border: 1px dashed #7D9E38;
							cursor: pointer;
							border-radius: 8px;
							color: #7D9E38;
							width: 90px;
							font-size: 32px;
							line-height: 90px;
							text-align: center;
							height: 90px;
							font-size: 14px;
							line-height: 1.8;
						}
						.el-upload .el-icon-plus {
							border: 1px dashed #7D9E38;
							cursor: pointer;
							border-radius: 8px;
							color: #7D9E38;
							width: 90px;
							font-size: 32px;
							line-height: 90px;
							text-align: center;
							height: 90px;
						}
						.el-upload__tip {
							color: #7D9E38;
						}
						.emailInput {
							border: 0;
							border-radius: 0;
							padding: 0 12px;
							box-shadow: 0 0 0px rgba(64, 158, 255, .5);
							margin: 0;
							outline: none;
							color: #666;
							background: #fff;
							width: 100%;
							font-size: 14px;
							height: 50px;
						}
						.emailInput:focus {
							border: 0px solid rgba(85, 170, 0, 1.0);
							padding: 0 12px;
							color: #7D9E38;
							width: 100%;
							font-size: 14px;
							height: 50px;
						}
						.el-btn {
							border: 0;
							cursor: pointer;
							padding: 0;
							margin: 0;
							color: #fff;
							font-size: 12px;
							line-height: 50px;
							border-radius: 0;
							box-shadow: 0 0 0px rgba(64, 158, 255, .5);
							outline: none;
							background: #7D9E38;
							width: 80px;
							height: 50px;
						}
						.el-btn:hover {
							opacity: 0.5;
						}
						
						.el-input__inner::placeholder {
							color: #999;
							font-size: 14px;
						}
						input::placeholder {
							color: #999;
							font-size: 14px;
						}
						.editor {
							width: 100%;
							height: auto;
						}
					}
				}
				.register-btn {
					width: 100%;
					order: 4;
				}
				.register-btn1 {
					width: 100%;
				}
				.register-btn2 {
					width: 100%;
				}
				.register_btn {
					border: 0;
					cursor: pointer;
					padding: 0 10px;
					margin: 20px auto 5px;
					color: #fff;
					display: block;
					font-size: 16px;
					border-radius: 0px;
					box-shadow: 0 0 0px rgba(64, 158, 255, .5);
					outline: none;
					background: #7D9E38;
					width: 80%;
					height: 44px;
				}
				.register_btn:hover {
					opacity: 0.5;
				}
				.has_btn {
					cursor: pointer;
					padding: 0 10%;
					color: rgba(159, 159, 159, 1);
					display: inline-block;
					text-decoration: none;
					width: 100%;
					font-size: 12px;
					line-height: 2;
					text-align: center;
				}
				.has_btn:hover {
					opacity: 0.5;
				}
			}
			.idea1 {
				background: red;
				display: none;
				width: 100%;
				height: 40px;
			}
			.idea2 {
				background: blue;
				display: none;
				width: 100%;
				height: 40px;
			}
		}
	}
	
	::-webkit-scrollbar {
		display: none;
	}
</style>
