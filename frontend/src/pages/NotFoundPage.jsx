import { Box, Heading, Text, Button, VStack, Image } from '@chakra-ui/react';
import { Link as RouterLink } from 'react-router-dom';
import Layout from '../components/layout/Layout';

/**
 * NotFoundPage component
 * 
 * @returns {JSX.Element} NotFoundPage component
 */
const NotFoundPage = () => {
  return (
    <Layout>
      <VStack spacing={8} textAlign="center" py={10}>
        <Heading as="h1" size="2xl" color="brand.600">
          404
        </Heading>
        <Text fontSize="xl">The page you are looking for does not exist.</Text>
        <Button as={RouterLink} to="/" colorScheme="brand" size="lg">
          Return to Home
        </Button>
      </VStack>
    </Layout>
  );
};

export default NotFoundPage; 