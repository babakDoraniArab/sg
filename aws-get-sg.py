#!/usr/bin/env python3
import argparse
import subprocess

# Define the constant region value
REGION = "eu-west-2"

def main():
    # Create a parser for command-line arguments
    parser = argparse.ArgumentParser(description="AWS EC2 Security Group List")
    
    # Add the --profile argument
    parser.add_argument("--profile", required=True, help="Name of the AWS CLI profile to use")
    
    # Add the --grep argument
    parser.add_argument("--grep", help="Filter the output using grep")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Retrieve the values from the command-line arguments
    profile_name = args.profile
    grep_filter = args.grep
    
    try:
        # Build the AWS CLI command
        command = f"aws ec2 describe-security-groups --query 'SecurityGroups[*].[GroupId,GroupName]' --output text --profile {profile_name} --region {REGION}"
        
        # Run the AWS CLI command
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check the command's exit status
        if result.returncode == 0:
            # Apply grep filter if provided
            if grep_filter:
                output_lines = result.stdout.split("\n")
                filtered_lines = [line for line in output_lines if grep_filter in line]
                print("\n".join(filtered_lines))
            else:
                print(result.stdout)
        else:
            print(f"Error: {result.stderr}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
