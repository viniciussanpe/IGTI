resource "aws_lambda_function" "decompresss3" {
  filename      = "../../functions/fn_extract_rais.zip"
  function_name = "${local.prefix}_igti_df_extract_rais"
  role          = aws_iam_role.lambda_decompress.arn
  handler       = "handler.handler"
  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  #source_code_hash = filebase64sha256("../functions/fn_example_script.zip")
  runtime     = "python3.8"
  timeout     = 30
  memory_size = 128
  // environment {
  //   variables = {
  //   }
  // }

  tags = local.common_tags

}
