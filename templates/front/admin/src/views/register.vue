<template>
	<div>
		<div class="register-container">
			<el-form v-if="pageFlag=='register'" ref="ruleForm" class="rgs-form animate__animated animate__backInLeft" :model="ruleForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">高校后勤报修系统设计与实现</div>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('zhanghao')?'required':''">账号：</div>
						<el-input  v-model="ruleForm.zhanghao"  autocomplete="off" placeholder="账号"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('xingming')?'required':''">姓名：</div>
						<el-input  v-model="ruleForm.xingming"  autocomplete="off" placeholder="姓名"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input  v-model="ruleForm.mima"  autocomplete="off" placeholder="密码"  type="password"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input  v-model="ruleForm.mima2" autocomplete="off" placeholder="确认密码" type="password" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="ruleForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in yonghuxingbieOptions"
								v-bind:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('shouji')?'required':''">手机：</div>
						<el-input  v-model="ruleForm.shouji"  autocomplete="off" placeholder="手机"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="3"
							:multiple="true"
							:fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
							@change="yonghutouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'">
						<div class="lable" :class="changeRules('weixiuzhanghao')?'required':''">维修账号：</div>
						<el-input  v-model="ruleForm.weixiuzhanghao"  autocomplete="off" placeholder="维修账号"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'">
						<div class="lable" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input  v-model="ruleForm.mima"  autocomplete="off" placeholder="密码"  type="password"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'">
						<div class="lable" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input  v-model="ruleForm.mima2" autocomplete="off" placeholder="确认密码" type="password" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'">
						<div class="lable" :class="changeRules('weixiuxingming')?'required':''">维修姓名：</div>
						<el-input  v-model="ruleForm.weixiuxingming"  autocomplete="off" placeholder="维修姓名"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'">
						<div class="lable" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="ruleForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in weixiurenyuanxingbieOptions"
								v-bind:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'">
						<div class="lable" :class="changeRules('lianxifangshi')?'required':''">联系方式：</div>
						<el-input  v-model="ruleForm.lianxifangshi"  autocomplete="off" placeholder="联系方式"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='weixiurenyuan'">
						<div class="lable" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="3"
							:multiple="true"
							:fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
							@change="weixiurenyuantouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'">
						<div class="lable" :class="changeRules('shenpizhanghao')?'required':''">审批账号：</div>
						<el-input  v-model="ruleForm.shenpizhanghao"  autocomplete="off" placeholder="审批账号"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'">
						<div class="lable" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input  v-model="ruleForm.mima"  autocomplete="off" placeholder="密码"  type="password"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'">
						<div class="lable" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input  v-model="ruleForm.mima2" autocomplete="off" placeholder="确认密码" type="password" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'">
						<div class="lable" :class="changeRules('shenpixingming')?'required':''">审批姓名：</div>
						<el-input  v-model="ruleForm.shenpixingming"  autocomplete="off" placeholder="审批姓名"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'">
						<div class="lable" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="ruleForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in shenpiyuanxingbieOptions"
								v-bind:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'">
						<div class="lable" :class="changeRules('lianxishouji')?'required':''">联系手机：</div>
						<el-input  v-model="ruleForm.lianxishouji"  autocomplete="off" placeholder="联系手机"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='shenpiyuan'">
						<div class="lable" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="3"
							:multiple="true"
							:fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
							@change="shenpiyuantouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<button type="button" class="r-btn" @click="login()">注册</button>
						</div>
						<div class="register-btn2">
							<div class="r-login" @click="close()">已有账号，直接登录</div>
						</div>
					</div>
				</div>
			</el-form>
		</div>
	</div>
</template>

<script>
	import 'animate.css'
export default {
	data() {
		return {
			ruleForm: {
			},
			forgetForm: {},
            pageFlag : '',
			tableName:"",
			rules: {},
            yonghuxingbieOptions: [],
            weixiurenyuanxingbieOptions: [],
            shenpiyuanxingbieOptions: [],
		};
	},
	mounted(){
		this.pageFlag = this.$route.query.pageFlag
		if(this.$route.query.pageFlag=='register'){
			
			let table = this.$storage.get("loginTable");
			this.tableName = table;
			if(this.tableName=='yonghu'){
				this.ruleForm = {
					zhanghao: '',
					xingming: '',
					mima: '',
					xingbie: '',
					shouji: '',
					touxiang: '',
				}
			}
			if(this.tableName=='weixiurenyuan'){
				this.ruleForm = {
					weixiuzhanghao: '',
					mima: '',
					weixiuxingming: '',
					xingbie: '',
					lianxifangshi: '',
					touxiang: '',
				}
			}
			if(this.tableName=='shenpiyuan'){
				this.ruleForm = {
					shenpizhanghao: '',
					mima: '',
					shenpixingming: '',
					xingbie: '',
					lianxishouji: '',
					touxiang: '',
				}
			}
			if ('yonghu' == this.tableName) {
				this.rules.zhanghao = [{ required: true, message: '请输入账号', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.xingming = [{ required: true, message: '请输入姓名', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('weixiurenyuan' == this.tableName) {
				this.rules.weixiuzhanghao = [{ required: true, message: '请输入维修账号', trigger: 'blur' }]
			}
			if ('weixiurenyuan' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('weixiurenyuan' == this.tableName) {
				this.rules.weixiuxingming = [{ required: true, message: '请输入维修姓名', trigger: 'blur' }]
			}
			if ('shenpiyuan' == this.tableName) {
				this.rules.shenpizhanghao = [{ required: true, message: '请输入审批账号', trigger: 'blur' }]
			}
			if ('shenpiyuan' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('shenpiyuan' == this.tableName) {
				this.rules.shenpixingming = [{ required: true, message: '请输入审批姓名', trigger: 'blur' }]
			}
			if ('shenpiyuan' == this.tableName) {
				this.rules.lianxishouji = [{ required: true, message: '请输入联系手机', trigger: 'blur' }]
			}
			this.yonghuxingbieOptions = "男,女".split(',')
			this.weixiurenyuanxingbieOptions = "男,女".split(',')
			this.shenpiyuanxingbieOptions = "男,女".split(',')
		}
	},
	created() {
	},
	destroyed() {
		  	},
	methods: {
		changeRules(name){
			if(this.rules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
		close(){
			this.$router.push({ path: "/login" });
		},
        yonghutouxiangUploadChange(fileUrls) {
            this.ruleForm.touxiang = fileUrls;
        },
        weixiurenyuantouxiangUploadChange(fileUrls) {
            this.ruleForm.touxiang = fileUrls;
        },
        shenpiyuantouxiangUploadChange(fileUrls) {
            this.ruleForm.touxiang = fileUrls;
        },

        // 多级联动参数


		// 注册
		login() {
			var url=this.tableName+"/register";
			if((!this.ruleForm.zhanghao) && `yonghu` == this.tableName){
				this.$message.error(`账号不能为空`);
				return
			}
			if((!this.ruleForm.xingming) && `yonghu` == this.tableName){
				this.$message.error(`姓名不能为空`);
				return
			}
			if((!this.ruleForm.mima) && `yonghu` == this.tableName){
				this.$message.error(`密码不能为空`);
				return
			}
			if((this.ruleForm.mima!=this.ruleForm.mima2) && `yonghu` == this.tableName){
				this.$message.error(`两次密码输入不一致`);
				return
			}
			if(`yonghu` == this.tableName && this.ruleForm.shouji &&(!this.$validate.isMobile(this.ruleForm.shouji))){
				this.$message.error(`手机应输入手机格式`);
				return
			}
            if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
            }
			if((!this.ruleForm.weixiuzhanghao) && `weixiurenyuan` == this.tableName){
				this.$message.error(`维修账号不能为空`);
				return
			}
			if((!this.ruleForm.mima) && `weixiurenyuan` == this.tableName){
				this.$message.error(`密码不能为空`);
				return
			}
			if((this.ruleForm.mima!=this.ruleForm.mima2) && `weixiurenyuan` == this.tableName){
				this.$message.error(`两次密码输入不一致`);
				return
			}
			if((!this.ruleForm.weixiuxingming) && `weixiurenyuan` == this.tableName){
				this.$message.error(`维修姓名不能为空`);
				return
			}
			if(`weixiurenyuan` == this.tableName && this.ruleForm.lianxifangshi &&(!this.$validate.isMobile(this.ruleForm.lianxifangshi))){
				this.$message.error(`联系方式应输入手机格式`);
				return
			}
            if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
            }
			if((!this.ruleForm.shenpizhanghao) && `shenpiyuan` == this.tableName){
				this.$message.error(`审批账号不能为空`);
				return
			}
			if((!this.ruleForm.mima) && `shenpiyuan` == this.tableName){
				this.$message.error(`密码不能为空`);
				return
			}
			if((this.ruleForm.mima!=this.ruleForm.mima2) && `shenpiyuan` == this.tableName){
				this.$message.error(`两次密码输入不一致`);
				return
			}
			if((!this.ruleForm.shenpixingming) && `shenpiyuan` == this.tableName){
				this.$message.error(`审批姓名不能为空`);
				return
			}
			if((!this.ruleForm.lianxishouji) && `shenpiyuan` == this.tableName){
				this.$message.error(`联系手机不能为空`);
				return
			}
			if(`shenpiyuan` == this.tableName && this.ruleForm.lianxishouji &&(!this.$validate.isMobile(this.ruleForm.lianxishouji))){
				this.$message.error(`联系手机应输入手机格式`);
				return
			}
            if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
            }
			this.$http({
				url: url,
				method: "post",
				data:this.ruleForm
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.$message({
						message: "注册成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							this.$router.replace({ path: "/login" });
						}
					});
				} else {
					this.$message.error(data.msg);
				}
			});
		}
	}
};
</script>

<style lang="scss" scoped>
.register-container {
	position: relative;
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
	.rgs-form {
		.rgs-form2 {
		width: 100%;
		}
		padding: 40px 10% 20px 180px;
		margin: 20px 0;
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
		.title {
			padding: 0 0px;
			margin: 0 0 20px 0;
			color: #fff;
			background: none;
			font-weight: 600;
			width: 100%;
			font-size: 22px;
			line-height: 30px;
			text-align: center;
		}
		.list-item {
			padding: 0 0 0 0px;
			margin: 0 0 26px;
			width: 100%;
			position: relative;
			height: auto;
			/deep/ .el-form-item__content {
				display: block;
			}
			.lable {
				padding: 0 5px 0 0;
				color: #fff;
				left: -120px;
				width: 120px;
				font-size: 16px;
				line-height: 34px;
				position: absolute !important;
				text-align: right;
			}
			.el-input {
				width: 100%;
			}
			.el-input /deep/ .el-input__inner {
				border: 0px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px;
				color: #666;
				background: rgba(0, 0, 0, .2);
				width: 100%;
				font-size: 14px;
				height: 38px;
			}
			.el-input /deep/ .el-input__inner:focus {
				border: 1px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px;
				outline: none;
				color: #666;
				background: #fff;
				width: 100%;
				font-size: 14px;
				height: 38px;
			}
			.el-input-number {
				width: 100%;
			}
			.el-input-number /deep/ .el-input__inner {
				text-align: center;
				border: 0px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px;
				color: #666;
				background: rgba(0, 0, 0, .2);
				width: 100%;
				font-size: 14px;
				height: 38px;
			}
			.el-input-number /deep/ .el-input__inner:focus {
				border: 1px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px;
				outline: none;
				color: #666;
				background: #fff;
				width: 100%;
				font-size: 14px;
				height: 38px;
			}
			.el-input-number /deep/ .el-input-number__decrease {
				display: none;
			}
			.el-input-number /deep/ .el-input-number__increase {
				display: none;
			}
			.el-select {
				width: 100%;
			}
			.el-select /deep/ .el-input__inner {
				border: 0px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px;
				color: #ccc;
				background: rgba(0, 0, 0, .2);
				width: 100%;
				font-size: 16px;
				height: 38px;
			}
			.el-select /deep/ .el-input__inner:focus {
				border: 1px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px;
				outline: none;
				color: #666;
				background: #fff;
				width: 100%;
				font-size: 16px;
				height: 38px;
			}
			.el-date-editor {
				width: 100%;
			}
			.el-date-editor /deep/ .el-input__inner {
				border: 0px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px 0 30px;
				color: #ccc;
				background: rgba(0, 0, 0, .2);
				width: 100%;
				font-size: 16px;
				height: 38px;
			}
			.el-date-editor /deep/ .el-input__inner:focus {
				border: 1px solid #efeff7;
				border-radius: 20px;
				padding: 0 10px 0 30px;
				outline: none;
				color: #666;
				background: #fff;
				width: 100%;
				font-size: 16px;
				height: 38px;
			}
			.el-date-editor.el-input {
				width: 100%;
			}
			/deep/ .el-upload--picture-card {
				background: transparent;
				border: 0;
				border-radius: 0;
				width: auto;
				height: auto;
				line-height: initial;
				vertical-align: middle;
			}
			/deep/ .upload .upload-img {
				border: 0px solid #efeff7;
				cursor: pointer;
				border-radius: 20px;
				color: #ccc;
				background: rgba(0, 0, 0, .2);
				width: 90px;
				font-size: 24px;
				line-height: 60px;
				text-align: center;
				height: 60px;
			}
			/deep/ .el-upload-list .el-upload-list__item {
				border: 0px solid #efeff7;
				cursor: pointer;
				border-radius: 20px;
				color: #ccc;
				background: rgba(0, 0, 0, .2);
				width: 90px;
				font-size: 24px;
				line-height: 60px;
				text-align: center;
				height: 60px;
			}
			/deep/ .el-upload .el-icon-plus {
				border: 0px solid #efeff7;
				cursor: pointer;
				border-radius: 20px;
				color: #ccc;
				background: rgba(0, 0, 0, .2);
				width: 90px;
				font-size: 24px;
				line-height: 60px;
				text-align: center;
				height: 60px;
			}
			/deep/ .el-upload__tip {
				color: #fff;
				font-size: 15px;
			}
			/deep/ .el-input__inner::placeholder {
				color: #ccc;
				font-size: 16px;
			}
			.required {
				position: relative;
			}
			.required::after{
				color: red;
				left: 110px;
				position: absolute !important;
				content: "*";
				order: -1;
			}
			.editor {
				background: #fff;
				width: 100%;
				height: auto;
			}
			.editor>.avatar-uploader {
				line-height: 0;
				height: 0;
			}
		}
		.list-item.email {
			input {
				border: 0px solid #efeff7;
				border-radius: 20px 0 0 20px;
				padding: 0 10px;
				margin: 0;
				color: #666;
				background: rgba(0, 0, 0, .2);
				flex: 1;
				width: 100%;
				font-size: 14px;
				height: 38px;
			}
			input:focus {
				border: 1px solid #efeff7;
				border-radius: 20px 0 0 20px;
				padding: 0 10px;
				outline: none;
				color: #666;
				background: #fff;
				width: 100%;
				font-size: 14px;
				height: 38px;
			}
			input::placeholder {
				color: #ccc;
				font-size: 16px;
			}
			button {
				border: 0px solid #efeff7;
				cursor: pointer;
				border-radius: 0 20px 20px 0;
				padding: 0;
				margin: 1px 0 0;
				color: #fff;
				background: #6a8b73;
				width: 150px;
				font-size: 15px;
				height: 38px;
			}
			button:hover {
				opacity: 1;
			}
		}
		.register-btn {
			width: 100%;
		}
		.register-btn1 {
			width: 100%;
		}
		.register-btn2 {
			width: 100%;
		}
		.r-btn {
			border: 0px solid rgba(0, 0, 0, 1);
			cursor: pointer;
			padding: 0 10px;
			margin: 20px auto 5px;
			color: #fff;
			font-weight: 600;
			display: block;
			letter-spacing: 8px;
			font-size: 16px;
			border-radius: 30px;
			background: linear-gradient(90deg, rgba(74,103,82,1) 0%, rgba(94,168,164,1) 100%),#6a8b73;
			width: 100%;
			height: 44px;
		}
		.r-btn:hover {
			opacity: 0.8;
		}
		.r-login {
			cursor: pointer;
			padding: 0;
			color: #fff;
			display: inline-block;
			text-decoration: underline;
			width: 100%;
			font-size: 15px;
			line-height: 40px;
			text-align: right;
		}
		.r-login:hover {
			opacity: 1;
		}
	}
}
	
	::-webkit-scrollbar {
	  display: none;
	}
</style>
