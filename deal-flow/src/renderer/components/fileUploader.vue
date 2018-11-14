<template>
    <div class="">
        <el-upload v-if="isImage"
              class="avatar-uploader uk-flex uk-flex-center uk-margin"
              action=""
              :show-file-list="false"
              :auto-upload="false"
              :on-change="getBase64"
              :on-success="handleAvatarSuccess"
              :before-upload="beforeAvatarUpload"
              :thumbnail-mode="true"
              >
              <img v-if="encoded" :src="encoded" class="avatar">
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
        <el-upload v-else
          class="upload-demo"
          drag
          action=""
          :on-change="getBase64"
          :before-upload="beforeUpload">
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
            <div class="el-upload__tip" slot="tip">jpg/png/pdf files with a size less than 50mb</div>
            <div class="">
                {{fileList}}
            </div><br>
        </el-upload>
        <br>
    </div>
</template>
<script>
export default {
    name: 'FileUploader',
    props: ['isImage', 'value'],
    data() {
        return {
            imageUrl: null,
            encoded: null,
            fileList: null
        }
    },
    methods: {
        getBase64(file, fl) {
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                console.log(file.raw);
                reader.readAsDataURL(file.raw);
                reader.onload = () => {
                    let encoded = reader.result.replace(/^data:(.*;base64,)?/, '');
                    if ((encoded.length % 4) > 0) {
                        encoded += '='.repeat(4 - (encoded.length % 4));
                    }
                    resolve(
                        this.encoded='data:'+ file.raw.type +';base64,'+encoded,
                        this.$emit('input', this.encoded)
                    );
                };
                reader.onerror = error => reject(error);
            });
        },
        handleAvatarSuccess(res, file) {
          this.imageUrl = "/static/" + file.raw.path.replace(/^.+static/,''); ;
          // this.form.avatar = this.imageUrl;
          console.log(  "IMAGE PATH: "+this.form.avatar);
          console.log(file.raw.path);
        },
        beforeAvatarUpload(file) {
          const isJPG = file.type === 'image/jpeg';
          const isLt2M = file.size / 1024 / 1024 < 2;

          if (!isJPG) {
            this.$message.error('Avatar picture must be JPG format!');
          }
          if (!isLt2M) {
            this.$message.error('Avatar picture size can not exceed 2MB!');
          }
          return isJPG && isLt2M;
        },
        beforeUpload(file) {
          const isLt2M = file.size / 1024 / 1024 < 2;

          if (!isLt2M) {
            this.$message.error('Upload can not exceed 2MB!');
          }
          return isLt2M;
        },
    }
}
</script>

<style lang="css">
</style>
