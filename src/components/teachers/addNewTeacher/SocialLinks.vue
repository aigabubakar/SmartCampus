<template>
    <div class="card h-100">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
            <h6 class="text-lg fw-semibold mb-0">Social Links</h6>
        </div>
        <div class="card-body p-20">
            <div class="row gy-3">
                <div class="col-xxl-3 col-xl-4 col-sm-6">
                    <div class="">
                        <label for="facebookLink" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Facebook
                        </label>
                        <input type="text" id="facebookLink" class="form-control" placeholder="Enter Facebook Link">
                    </div>
                </div>
                <div class="col-xxl-3 col-xl-4 col-sm-6">
                    <div class="">
                        <label for="linkedInLink" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">LinkedIn
                        </label>
                        <input type="text" id="linkedInLink" class="form-control" placeholder="Enter LinkedIn Link">
                    </div>
                </div>
                <div class="col-xxl-3 col-xl-4 col-sm-6">
                    <div class="">
                        <label for="instagramLink" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Instagram
                        </label>
                        <input type="text" id="instagramLink" class="form-control" placeholder="Enter Instagram Link">
                    </div>
                </div>
                <div class="col-xxl-3 col-xl-4 col-sm-6">
                    <div class="">
                        <label for="youTubeLink" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">YouTube
                        </label>
                        <input type="text" id="youTubeLink" class="form-control" placeholder="Enter YouTube Link">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "SocialLinks"
}
</script>
