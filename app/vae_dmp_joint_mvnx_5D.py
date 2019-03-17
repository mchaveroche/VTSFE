from .models.vae_dmp_2D import VAE_DMP_2D

vae_dmp_joint_mvnx_5D = VAE_DMP_2D()
vae_dmp_joint_mvnx_5D.set_data_config(["jointAngle"], "MVNX")

vae_dmp_joint_mvnx_5D.VTSFE_PARAMS["vae_architecture"]["n_z"] = 5
